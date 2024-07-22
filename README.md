
# Context Aware AI Assistant
This is a sophisticated AI assistant designed to enhance user interactions by leveraging the advanced capabilities of OpenAI's GPT-4o model. The project demonstrates two different architectural approaches to building an AI assistant: a **straightforward direct interaction** with the GPT-4o API (Version 1) and a **multi-agent system** using the CrewAI framework (Version 2).
- [README v1](https://github.com/lemberck/obot/blob/master/v1/README.md)
- [README v2](https://github.com/lemberck/obot/blob/master/v2/README.md)

## Project Structure
```bash
OBOT/
├── img/ 
│   └── ...
├── v1/ # folder containing version 1 of tha assistant - gpt API approach
│   ├── dev/
│   │   └── dev.py
│   ├── flagged/ 
│   ├── logs/
│   │   └── v1_app.log
│   └── src/
│       ├── chat_history.txt # can be dowloaded by the user
│       ├── gpt_interaction.py
│       ├── gradio_interface.py
│       ├── main.py
│       └── utils.py
├── v2/ # folder containing version 2 of tha assistant - multiagent approach
│   ├── dev/
│   │   └── dev.py
│   ├── flagged/ 
│   ├── logs/
│   │   └── v2_app.log
│   └── src/
│       ├── chat_history.txt # can be dowloaded by the user
│       ├── crew_setup.py
│       ├── gradio_interface.py
│       ├── main.py
│       └── utils.py
├── .env # edited env_template
├── .gitignore
├── poetry.lock
└── pyproject.toml
```

## Overview

### Context-Aware Interactions
Both versions maintain a conversation history to ensure context-aware interactions. By keeping track of previous exchanges, the assistant can provide coherent responses and generate relevant follow-up questions, making the conversation more meaningful and personalized.

### Version 1 - Simplified Perplexity AI Assistant
This version provides a straightforward approach by interacting directly with OpenAI's GPT-4o API. It is designed to be simple and easy to set up while providing powerful AI capabilities for generating responses and follow-up questions. This approach ensures quick and efficient responses by maintaining a conversation history, which allows the AI to provide context-aware answers and generate relevant follow-up questions.

#### Features
- Direct Interaction with GPT-4o API: Utilizes OpenAI's GPT-4o model to generate high-quality responses and follow-up questions.
- Large Language Model Processing: Powered by OpenAI's GPT-4o model to provide high-quality responses and follow-up questions.
- User-Friendly Interface: Implements Gradio for an intuitive and interactive user experience.
- Memory Management: Maintains conversation history for context-aware interactions.
- Download Conversation History: Allows users to download their conversation history as a text file.
- Logging and Error Handling: Uses Loguru for robust logging and error management.

#### Pros
- Simplicity: Easy to set up and use.
- Efficiency: Direct interaction with the GPT-4o API ensures quick responses.
- Context Awareness: Maintains conversation history to provide coherent and context-aware interactions.
#### Cons
- Scalability: Limited by the capabilities of a single AI model without multi-agent collaboration.
- Flexibility: Less flexible in handling complex interactions compared to multi-agent systems.
- Modularity: Less modular compared to multi-agent systems, making it harder to extend functionality.

### Version 2 - Multi-Agent AI Assistant with CrewAI
Version 2 introduces a more advanced architecture by leveraging the CrewAI framework, which is based on LangChain agents. This version decomposes the assistant into multiple specialized agents, each responsible for a specific task. The multi-agent setup enhances the flexibility and modularity of the assistant, allowing for more complex and dynamic interactions.

#### Features
- Multi-Agent Architecture: Utilizes CrewAI framework to create seamless interactions between multiple agents.
- Large Language Model Processing: Powered by OpenAI's GPT-4o model to provide high-quality responses and follow-up questions.
- Memory Management: Maintains conversation history for context-aware interactions.
- User-Friendly Interface: Implements Gradio for an intuitive and interactive user experience.
- Download Conversation History: Allows users to download their conversation history as a text file.
- Logging and Error Handling: Uses Loguru for robust logging and error management.

#### Agents
- Query Responder:

    - Role: Provide accurate and helpful responses to user queries.
    - Goal: Assist users by addressing their needs and answering their questions effectively.
    - Backstory: A highly knowledgeable assistant with expertise in various domains, dedicated to ensuring users have the best experience by providing clear and objective responses based on the conversation history.
- Question Generator:

    - Role: Generate insightful follow-up questions based on user queries and responses.
    - Goal: Enhance the conversation by suggesting questions that delve deeper into the topic at hand.
    - Backstory: An analytical mind skilled at generating relevant follow-up questions, focusing on being objective and ensuring the questions are useful for the user.

#### Pros
- Scalability: Enhanced by the use of multiple agents collaborating to handle complex tasks.
- Flexibility: Easier to extend with new functionalities by adding or modifying agents.
- Modularity: Each agent can be developed, tested, and maintained independently.
- Complex Task Handling: Capable of managing more sophisticated interactions through collaboration between agents.
#### Cons
- Complexity: More complex to set up and manage compared to a single-model approach.
- Resource Intensive: Requires more computational resources due to the multi-agent architecture.
- Performance: Potentially slower response times due to inter-agent communication overhead.
    - This can potentially be mitigated with more resource power.


## Conclusion
This repo provides two distinct approaches to building an AI assistant, each with its own strengths and trade-offs. Version 1 offers simplicity and efficiency through direct interaction with the GPT-4o API, making it ideal for straightforward applications. Version 2, on the other hand, leverages a multi-agent system to provide greater modularity and flexibility, suitable for more complex and dynamic interactions. By understanding the pros and cons of each approach, developers can choose the one that best fits their needs and expand upon it to create robust and intelligent AI assistants.