from google.ai.generativelanguage_v1beta.types import content
import google.generativeai as genai
import gradio as gr
import os 
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API'))

model = genai.GenerativeModel('gemini-1.5-flash')

def gemini_chatbot(message, history):
    formatted_history = []
    for each in history:
        formatted_history.append(content.Content(parts = [{"text": each[0]}], role = "user"))
        formatted_history.append(content.Content(parts = [{"text": each[1]}], role = "model"))
    chat = model.start_chat(history=formatted_history)
    response = chat.send_message(message)
    return response.text

demo_chatbot = gr.ChatInterface(gemini_chatbot, title="Gemini Chatbot", description = "Start Chatting")
demo_chatbot.launch() 