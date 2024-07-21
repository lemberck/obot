import os
import openai
import gradio as gr
from loguru import logger
from dotenv import load_dotenv

# Set up logging
logger.add("logs/v1_app.log", rotation="1 day", retention="1 week", compression="zip")

# Set up openAI api key
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
openai.api_key = os.environ["OPENAI_API_KEY"]

def generate_response(user_input, conversation_history):
    """
    Generate a response from the OpenAI GPT-4o model based on user input and conversation history.

    Args:
        user_input (str): The user's input query.
        conversation_history (list): The history of the conversation as a list of message dictionaries.

    Returns:
        tuple: A tuple containing the assistant's reply, follow-up questions, and the updated conversation history.
    """
    try:
        # append user input to the conversation history
        conversation_history.append({"role": "user", "content": user_input})

        # Call OpenAI's GPT-4o model
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=conversation_history,
            #max_tokens=1000,
            temperature=0.5,
        )

        # Get the model's reply
        assistant_reply = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": assistant_reply})

        # Log the conversation
        logger.info(f"User: {user_input}")
        logger.info(f"Assistant: {assistant_reply}")

        # Generate follow-up questions
        follow_up_questions = generate_follow_up_questions(user_input, assistant_reply, conversation_history)

        return assistant_reply, follow_up_questions, conversation_history

    except Exception as e:
        logger.error(f"Error occurred: {e}")
        return "An error occurred while processing your request.", [], conversation_history

def generate_follow_up_questions(user_input, assistant_reply,conversation_history):
    """
    Generate follow-up questions based on the user's input and the assistant's response.

    Args:
        user_input (str): The user's input query.
        assistant_reply (str): The assistant's response to the user's input.
        conversation_history (list): The history of the conversation as a list of message dictionaries.

    Returns:
        str: The generated follow-up questions formatted according to the specified template.
    """
    try:
        follow_up_prompt = f"""
        Based on the user's question '{user_input}' and the assistant's response '{assistant_reply}', generate three follow-up questions.
        The questions must be short, objective and focus on being useful for the user by using the context of the assistant response and 
        the user's intention.
        The follow-up questions must be generated from the user's point of view, as if the user was asking you.
        The output must follow the template below:
        ### Suggested follow-up questions:
        - question 1
        - question 2
        - question 3
        """
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generate questions relevant to the user."},
                {"role": "user", "content": follow_up_prompt}
            ],
            max_tokens=200,
            temperature=0.7
        )

        follow_up_questions = response.choices[0].message.content
        return follow_up_questions
    except Exception as e:
        logger.error(f"Error occurred while generating follow-up questions: {e}")
        return []
    
def format_conversation(conversation_history):
    """
    Format the conversation history into a readable string format.

    Args:
        conversation_history (list): The history of the conversation as a list of message dictionaries.

    Returns:
        str: The formatted conversation history with each entry on a new line, prefixed by the role (User or Assistant).
    """
    return "\n".join([f"{entry['role'].capitalize()}: {entry['content']}" for entry in conversation_history])

def save_conversation_to_file(conversation_history):
    """
    Save the formatted conversation history to a text file.

    Args:
        conversation_history (list): The history of the conversation as a list of message dictionaries.

    Returns:
        str: The file path where the conversation history is saved.
    """
    full_conversation = format_conversation(conversation_history)
    file_path = "v1/dev/chat_history.txt"
    with open(file_path, "w") as file:
        file.write(full_conversation)
    return file_path

### Create a Gradio interface
def process_query(user_input, history):
    """
    Process the user's query, generate a response, and save the conversation history.

    Args:
        user_input (str): The user's input query.
        history (list): The history of the conversation as a list of message dictionaries.

    Returns:
        tuple: A tuple containing the full formatted conversation, follow-up questions, updated conversation history, and the file path of the saved conversation history.
    """
    assistant_reply, follow_up_questions, updated_history = generate_response(user_input, history)
    full_conversation = format_conversation(updated_history)
    chat_history_file = save_conversation_to_file(updated_history)
    
    return full_conversation, follow_up_questions, updated_history, chat_history_file

# set up the interface and launch it
demo = gr.Interface(
    fn=process_query,
    inputs=[gr.Textbox(label="Enter your query"), gr.State([])],  # State input to hold conversation history
    outputs=[
        gr.Textbox(label="Conversation History", interactive=False, lines=20), 
        gr.Textbox(label="Follow-up Questions", interactive=False, lines=5), 
        gr.State([]),  # Single state output for updated history
        gr.File(label="Download Chat History")  # File output for downloading chat history
    ],
    title="Simplified Perplexity AI Assistant",
    description="Ask anything and get responses powered by OpenAI's GPT-4o.",
    flagging_dir='flagged',
)
demo.launch(share=True)
