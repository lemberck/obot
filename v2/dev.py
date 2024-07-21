from crewai import Agent, Task, Crew
from dotenv import load_dotenv
import os
from loguru import logger
import gradio as gr

# init vars
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# set up logging
logger.add("logs/v2_app.log", rotation="1 day", retention="1 week", compression="zip")

# ######################## Get user query Agent
get_user_query_agent = Agent(
    role="Get user query",
    goal="Capture the user query.",
    backstory=(
        "You are the first point of contact. Your job is to capture the user query," 
        "and ensure it is properly handled by the next agent in the workflow."
    ),
    temperature=0,
    verbose=True,
    allow_delegation=False,
)

#### Get user query Task
get_user_query_task = Task(
    description=(
        "Capture the user's query {user_query} and pass it to the next agent for further processing."
    ),
    expected_output="{user_query}",
    agent=get_user_query_agent,
    human_input=False,
    max_iter = 2,
)

######################## Answer User Agent
answer_user_agent = Agent(
    role="Query Responder",
    goal="Provide accurate and helpful responses to user queries.",
    backstory=(
        "You are a highly knowledgeable assistant with expertise in various domains. "
        "Your primary focus is to assist users by providing accurate and helpful responses "
        "to their queries and based on the conversation history {conversation_history}. " 
        "You are dedicated to ensuring users have the best experience "
        "by addressing their needs and answering their questions effectively and in an objective way."
    ),
    temperature=0.5,
    verbose=True,
    allow_delegation=False,
)

#### Answer User Task
answer_user_task = Task(
    description=(
        "You will process user queries {user_query} and provide accurate, helpful responses based also in the conversation history. "
        "Ensure that the responses are clear and address the user's needs effectively. "
        "Maintain a friendly tone throughout the interaction and be objective with the answers."
        "Conversation history: {conversation_history}."
    ),
    expected_output="A clear and helpful response to the user's query.",
    agent=answer_user_agent,
    human_input=False,
)

######################## Generate questions Agent
generate_questions_agent = Agent(
    role="Question Generator",
    goal="Generate 3 insightful follow-up questions based on user queries and responses.",
    backstory=(
        "You have a keen analytical mind and are skilled at generating relevant follow-up questions. "
        "Your role is to enhance the conversation by suggesting questions that delve deeper into the "
        "topic at hand. You focus on being objective and ensuring the questions are useful for the user."
    ),
    temperature=0.5,
    verbose=True,
    allow_delegation=False,
)

#### Generate questions Task
generate_questions_task = Task(
    description=(
        "Based on the current user's query {user_query} and the previous task response, generate three insightful follow-up questions. "
        "Ensure that the questions are short, objective, and useful for the user, taking into account "
        "the context of the conversation."
        "Make sure the questions are generated from the user's point of view, as if the user was asking them to you."
        "Do not generate questions that are not as if the user themselves are asking, based on the context."
    ),
    expected_output=(
        "- question 1\n"
        "- question 2\n"
        "- question 3"
    ),
    agent=generate_questions_agent,
    human_input=False,
    context=[answer_user_task],
)

######################## Kickoff Crew
# Example input
example_input = {}

crew = Crew(
    agents=[
        #get_user_query_agent,
        answer_user_agent,
        generate_questions_agent,
    ],

    tasks=[
        #get_user_query_task,
        answer_user_task,
        generate_questions_task,
    ],
    verbose=0,
    memory=True,  # store and pass information among agents

)

############ Execute the crew once 
#result = crew.kickoff(inputs=example_input)

############ Execute the crew in a loop
# def run_crew_in_loop():
#     # Initial introduction
#     print("Hello, I can answer your queries and suggest follow-up questions. Just ask and I'll generate the best answer for your request.")

#     conversation_history = []

#     while True:
#         user_input = input("You: ")

#         # Update conversation history with user input
#         conversation_history.append({"role": "user", "content": user_input})
#         print(conversation_history)

#         # Execute the crew with the updated conversation history
#         crew.kickoff(inputs={'user_query': user_input, 'conversation_history': conversation_history})

#         # Get the outputs
#         answer_output = answer_user_task.output.raw
#         questions_output = generate_questions_task.output.raw

#         # Update conversation history with agent responses
#         conversation_history.append({"role": "assistant", "content": answer_output})
#         #conversation_history.append({"role": "assistant", "content": questions_output})

#         # Print the outputs
#         print(f"Assistant: {answer_output}")
#         print(f"Follow-up Questions: \n{questions_output}")

# # Start the crew loop
# run_crew_in_loop()

######################## Gradio interface
def process_query(user_input, conversation_history):
    """
    Process the user's query, generate a response, and follow-up questions using CrewAI.

    Args:
        user_input (str): The user's input query.
        conversation_history (list): The history of the conversation as a list of message dictionaries.

    Returns:
        tuple: A tuple containing the assistant's reply, follow-up questions, and the updated conversation history.
    """
    try:
        # Append user input to the conversation history
        conversation_history.append({"role": "user", "content": user_input})

        # Execute the crew with the updated conversation history
        crew.kickoff(inputs={'user_query': user_input, 'conversation_history': conversation_history})
        
        answer_output = answer_user_task.output.raw
        questions_output = generate_questions_task.output.raw

        # Append the outputs to the conversation history
        conversation_history.append({"role": "assistant", "content": answer_output})
        # conversation_history.append({"role": "assistant", "content": questions_output})

        # Log the conversation
        logger.info(f"User: {user_input}")
        logger.info(f"Assistant: {answer_output}")
        logger.info(f"Follow-up Questions: \n{questions_output}")

        return answer_output, questions_output, conversation_history

    except Exception as e:
        logger.error(f"Error occurred: {e}")
        return "An error occurred while processing your request.", "", conversation_history

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
    file_path = "v2/chat_history.txt"
    with open(file_path, "w") as file:
        file.write(full_conversation)
    return file_path

### Create a Gradio interface
def process_query_interface(user_input, history):
    """
    Process the user's query, generate a response, and save the conversation history.

    Args:
        user_input (str): The user's input query.
        history (list): The history of the conversation as a list of message dictionaries.

    Returns:
        tuple: A tuple containing the full formatted conversation, follow-up questions, updated conversation history, and the file path of the saved conversation history.
    """
    # init conversation history
    if history is None:
        history = []

    assistant_reply, follow_up_questions, updated_history = process_query(user_input, history)
    full_conversation = format_conversation(updated_history)
    chat_history_file = save_conversation_to_file(updated_history)
    
    return full_conversation, follow_up_questions, updated_history, chat_history_file

# Set up the interface and launch it
demo = gr.Interface(
    fn=process_query_interface,
    inputs=[gr.Textbox(label="Enter your query"), gr.State([])],  # State input to hold conversation history
    outputs=[
        gr.Textbox(label="Conversation History", interactive=False, lines=20), 
        gr.Textbox(label="Follow-up Questions", interactive=False, lines=5), 
        gr.State([]),  # Single state output for updated history
        gr.File(label="Download Chat History")  # File output for downloading chat history
    ],
    title="Multi-Agent AI Assistant",
    description="Ask anything and get responses powered by CrewAI with multi-agent support.",
    flagging_dir='v2/flagged',
)
demo.launch(share=True)