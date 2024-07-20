
# Simplified Perplexity AI Assistant - Version 1

This application is a simplified AI assistant powered by OpenAI's GPT-4o model. It uses Gradio to provide a user-friendly web interface where users can interact with the AI assistant, receive responses, see follow-up questions bsed on chat context and current query, and download their conversation history.

## Project Structure

```
obot/
├── logs/
├── v1/
│   ├── flagged/
│   ├── app.py
│   ├── chat_history.txt
├── .env_template
├── .gitignore
├── pyproject.toml
├── poetry.lock
```

## Setup Instructions

### Prerequisites

- Python 3.10
- Poetry for dependency management

### Environment Configuration

1. **Clone the repository:**
   ```sh
   git clone <repository_url>
   cd obot/v1
   ```

2. **Create a virtual environment and install dependencies:**
   ```sh
   poetry install --no-root
   ```

3. **Set up environment variables:**
   - Create a `.env` file in the root directory based on the `.env_template`.
   - Add your OpenAI API key to the `.env` file:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

### Running the Application

1. **Navigate to the `v1` directory:**
   ```sh
   cd v1
   ```

2. **Run the application:**
   ```sh
   python app.py
   ```

3. **Access the web interface:**
   - After running the application, it will provide a local URL (e.g., `http://127.0.0.1:7860`) and a public URL for accessing the interface, which can also be shared with the team. Open the provided URL in a web browser to start interacting with the AI assistant.

### Features

- **Interactive Chat Interface:** Type your queries and receive responses from the AI assistant.
- **Follow-up Questions:** The assistant generates follow-up questions based on the conversation context and the user current query.
- **Download Conversation History:** Download the entire conversation history as a text file.

### Logs

- Logs are stored in the `logs/` directory and are rotated daily with a retention period of one week and compressed to save space.

### Flagged Content

- Flagged conversations are stored in the `v1/flagged/` directory.