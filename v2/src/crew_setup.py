import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from loguru import logger

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
logger.add("logs/v2_app.log", rotation="1 day", retention="1 week", compression="zip")

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

######################## Crew

crew = Crew(
    agents=[
        answer_user_agent,
        generate_questions_agent,
    ],

    tasks=[
        answer_user_task,
        generate_questions_task,
    ],
    verbose=0,
    memory=True,
)

