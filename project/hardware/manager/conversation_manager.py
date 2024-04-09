"""ConversationManager Class"""
import os
from openai import OpenAI
from dotenv import load_dotenv

client = OpenAI() # initialize openai connection
load_dotenv() # bring env variables in for os

OPENAI_KEY = os.environ(['OPENAI_KEY']) # grab api key

class ConversationManager:
    """Manages User-ChatGPT communication"""
    def __init__(self, model_name="gpt-3.5-turbo-0125", ai_key = OPENAI_KEY):
        # Initialize OpenAI API with model
        self.ai_key = ai_key
        self.model_name = model_name

    def respond(self, user_input: list) -> str:
        """Generate response using OpenAI API"""

        response = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            response_format = { "type": "json_object" },
            messages = [
                user_input
            ]
        )
        return response.choices[0].text.strip()

    # Other methods for conversation management...
