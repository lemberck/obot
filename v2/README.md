
# Multi-Agent AI Assistant with CrewAI and GPT-4o

This project is an advanced AI assistant application that leverages the power of CrewAI's multi-agent architecture and OpenAI's GPT-4o model. The assistant is designed to process user queries, provide accurate and helpful responses, and generate insightful follow-up questions.

## Features

- **Multi-Agent Architecture**: Utilizes CrewAI framework to create a seamless interaction between multiple agents.
- **Large Language Model Processing**: Powered by OpenAI's GPT-4o model to provide high-quality responses and follow-up questions.
- **Memory Management**: Maintains conversation history for context-aware interactions.
- **User-Friendly Interface**: Implements Gradio for an intuitive and interactive user experience.
- **Logging and Error Handling**: Uses Loguru for robust logging and error management.

## Project Structure
```bash
OBOT/
├── logs/
│   └── v2_app.log # application logs for debugging
├── v2/
│   ├── dev/
|   |   └── dev.py
│   ├── flagged/ # stores interactions flagged by the user
│   └── src/
│       ├── chat_history.txt # can be downloaded by the user
│       ├── crew_setup.py
│       ├── gradio_interface.py
│       ├── main.py
│       └── utils.py
├── .env # edited env_template
├── .gitignore
├── poetry.lock
└── pyproject.toml
```

## Agents

This project uses a multi-agent architecture to handle different tasks effectively:

1. **Query Responder**: 
   - **Role**: Provide accurate and helpful responses to user queries.
   - **Goal**: Assist users by addressing their needs and answering their questions effectively.
   - **Backstory**: A highly knowledgeable assistant with expertise in various domains, dedicated to ensuring users have the best experience by providing clear and objective responses based on the conversation history.

2. **Question Generator**: 
   - **Role**: Generate insightful follow-up questions based on user queries and responses.
   - **Goal**: Enhance the conversation by suggesting questions that delve deeper into the topic at hand.
   - **Backstory**: An analytical mind skilled at generating relevant follow-up questions, focusing on being objective and ensuring the questions are useful for the user.

## Context-Aware Interactions

The assistant maintains a conversation history to ensure context-aware interactions. By keeping track of previous exchanges, the assistant can provide coherent responses and generate relevant follow-up questions, making the conversation more meaningful and personalized.

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/lemberck/obot.git
    cd obot/v2
    ```

2. **Install the dependencies and Activate a Virtual Environment using Poetry**:
    ```sh
    poetry install --no-root
    poetry shell
    ```

3. **Set Up Environment Variables**:
    Copy the `.env_template` to `.env` and fill in your OpenAI API key:
    ```sh
    cp .env_template .env
    ```
    Then, edit the `.env` file to include your OpenAI API key:
    ```env
    OPENAI_API_KEY='your_openai_api_key'
    ```

## Usage

### Running the Application

To start the application, run the following command:

```sh
python src/main.py
```

> Gradio will also generate a public link that can be shared, functional for 72h.

### Interacting with the Assistant
- Enter your query in the input textbox.
- The assistant will process your query, provide a response, and suggest follow-up questions.
- The conversation history and follow-up questions will be displayed in the interface.
- You can download the conversation history at any time.

![multiagent-ui-preview](https://github.com/lemberck/obot/blob/master/img/v2-multiagent.png)

### Error Handling and Logging
The application uses Loguru for logging and error handling. Log files are stored in `logs/v2_app.log`  and can be reviewed for debugging and monitoring purposes.