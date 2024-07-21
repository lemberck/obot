from gpt_interaction import generate_response
from loguru import logger

def process_query(user_input, history):
    """
    Process the user's query, generate a response, and save the conversation history.

    Args:
        user_input (str): The user's input query.
        history (list): The history of the conversation as a list of message dictionaries.

    Returns:
        tuple: A tuple containing the full formatted conversation, follow-up questions, updated conversation history, and the file path of the saved conversation history.
    """
    try:
        assistant_reply, follow_up_questions, updated_history = generate_response(user_input, history)
        full_conversation = format_conversation(updated_history)
        chat_history_file = save_conversation_to_file(updated_history)
        
        # Log the conversation
        logger.info(f"User: {user_input}")
        logger.info(f"Assistant: {assistant_reply}")
        logger.info(f"Follow-up Questions: \n{follow_up_questions}")

        return full_conversation, follow_up_questions, updated_history, chat_history_file

    except Exception as e:
        logger.error(f"Error occurred in process_query: {e}")
        return "An error occurred while processing your request.", "", history, ""

def format_conversation(conversation_history):
    """
    Format the conversation history into a readable string format.

    Args:
        conversation_history (list): The history of the conversation as a list of message dictionaries.

    Returns:
        str: The formatted conversation history with each entry on a new line, prefixed by the role (User or Assistant).
    """
    try:
        return "\n".join([f"{entry['role'].capitalize()}: {entry['content']}" for entry in conversation_history])
    except Exception as e:
        logger.error(f"Error in formatting conversation: {e}")
        return ""

def save_conversation_to_file(conversation_history):
    """
    Save the formatted conversation history to a text file.

    Args:
        conversation_history (list): The history of the conversation as a list of message dictionaries.

    Returns:
        str: The file path where the conversation history is saved.
    """
    try:
        full_conversation = format_conversation(conversation_history)
        file_path = "src/chat_history.txt"
        with open(file_path, "w") as file:
            file.write(full_conversation)
        return file_path
    except Exception as e:
        logger.error(f"Error in saving conversation to file: {e}")
        return ""
