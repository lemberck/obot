import gradio as gr
from utils import process_query

# Set up the interface and launch it
demo = gr.Interface(
    fn=process_query,
    inputs=[gr.Textbox(label="Enter your query"), gr.State([])], 
    outputs=[
        gr.Textbox(label="Conversation History", interactive=False, lines=20), 
        gr.Textbox(label="Follow-up Questions", interactive=False, lines=5), 
        gr.State([]),  
        gr.File(label="Download Chat History")
    ],
    title="Simplified Perplexity AI Assistant",
    description="Ask anything and get responses powered by OpenAI's GPT-4o.",
    flagging_dir='flagged',
)

def launch_interface():
    demo.launch(share=True)
