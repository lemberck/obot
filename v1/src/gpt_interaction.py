import openai
from loguru import logger

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

        # GPT-4o model setup
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=conversation_history,
            temperature=0.5,
        )

        assistant_reply = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": assistant_reply})

        # log the conversation
        logger.info(f"User: {user_input}")
        logger.info(f"Assistant: {assistant_reply}")

        
        follow_up_questions = generate_follow_up_questions(user_input, assistant_reply, conversation_history)

        return assistant_reply, follow_up_questions, conversation_history

    except Exception as e:
        logger.error(f"Error occurred: {e}")
        return "An error occurred while processing your request.", [], conversation_history

def generate_follow_up_questions(user_input, assistant_reply, conversation_history):
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
