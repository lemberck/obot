
# Simplified Perplexity AI Assistant - Version 1

This project is a straightforward AI assistant application that interacts directly with OpenAI's GPT-4o model. The assistant is designed to process user queries, provide accurate and helpful responses, and generate insightful follow-up questions. It uses Gradio to provide a user-friendly web interface where users can interact with the AI assistant, receive responses, see follow-up questions based on chat context and current query, and download their conversation history.

## Features
- **Direct Interaction with GPT-4o API**: Utilizes OpenAI's GPT-4o model to generate high-quality responses and follow-up questions.
- **User-Friendly Interface**: Implements Gradio for an intuitive and interactive user experience.
- **Memory Management**: Maintains conversation history for context-aware interactions.
- **Download Conversation History:** Download the entire conversation history as a text file.
- **Logging and Error Handling**: Uses Loguru for robust logging and error management.

## Project Structure

```bash
OBOT/
├── v1/
│   ├── dev/
│   │   └── dev.py
│   ├── .env # use env_template as a base
│   ├── poetry.lock
│   ├── pyproject.toml
│   ├── flagged/ # stores interactions flagged by the user
│   └── src/
│       ├── chat_history.txt # can be downloaded by the user
│       ├── generate_response.py
│       ├── gradio_interface.py
│       ├── main.py
│       └── utils.py
├── .env_template
└── .gitignore
```
## Context-Aware Interactions

The assistant maintains a conversation history to ensure context-aware interactions. By keeping track of previous exchanges, the assistant can provide coherent responses and generate relevant follow-up questions, making the conversation more meaningful and personalized.


## Setup Instructions

### Prerequisites

- Python 3.10
- Poetry for dependency management
- Open AI API Key

### Environment Configuration

1. **Clone the repository and open your code IDE in the version directory:**:
   ```sh
   git clone https://github.com/lemberck/obot.git
   cd obot/v1
   ```

2. **Install the dependencies and Activate a Virtual Environment using Poetry**:
   ```sh
   poetry install --no-root
   poetry shell
   ```

3. **Set up environment variables:**
   - Create a `.env` file **inside v1 directory**. Use `.env_template` as a base.
   - Add your OpenAI API key to the `.env` file:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```
   > Note: Must keep OPENAI_MODEL_NAME

## Usage

### Running the Application

To start the application, run the following command:

```sh
python src/main.py
```

### Interacting with the Assistant
- Enter your query in the input textbox.
- The assistant will process your query, provide a response, and suggest follow-up questions.
- The conversation history and follow-up questions will be displayed in the interface.
- You can download the conversation history at any time.

![gptapi-ui-preview](https://github.com/lemberck/obot/blob/master/img/v1-gptapi.png)

### Error Handling and Logging
The application uses Loguru for logging and error handling. Log files are stored in `logs/v1_app.log`  and can be reviewed for debugging and monitoring purposes.