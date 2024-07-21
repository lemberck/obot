import gradio as gr
from loguru import logger
from utils import process_query_interface

logger.add("logs/v2_app.log", rotation="1 day", retention="1 week", compression="zip")

# Set up the interface and launch it
demo = gr.Interface(
    fn=process_query_interface,
    inputs=[gr.Textbox(label="Enter your query"), gr.State([])],
    outputs=[
        gr.Textbox(label="Conversation History", interactive=False, lines=20), 
        gr.Textbox(label="Follow-up Questions", interactive=False, lines=5), 
        gr.State([]),
        gr.File(label="Download Chat History")
    ],
    title="Multi-Agent AI Assistant",
    description="Ask anything and get responses powered by CrewAI with multi-agent support.",
    flagging_dir='flagged',
)
