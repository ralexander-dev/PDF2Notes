import openai
from dotenv import load_dotenv
import myKeys as mk
import os

# Function to load the API key from the .env file.
def configure():
    load_dotenv()

openai.api_key = os.getenv('gpt_key')
messages = [{"role": "system", "content": 
            "Extract the important information to provide informative notes which detail the important information and disregard any unnecessary information. The notes should exlude any sort of practice questions which may be included in the text provided to you. The notes should be written in a clear and concise format, segment notes into bullet point sections and use headings to separate different topics. Your reply will be saved to a .docx file, with this in mind be sure to format the notes accordingly to ensure that they are neatly presented."}]

# This function takes text input read from the pdf and returns the ChatGPT reply. 
def CustomGPT(text):
    messages.append({"role":"user", "content": text})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo-16k",
        messages = messages
    )
    ChatGPT_Reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_Reply})
    return ChatGPT_Reply
