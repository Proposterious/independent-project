"""DataManager Class"""
import os
import time
import json
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
from utils.file_utils import read_users
from utils.file_utils import get_specified_user
from utils.file_utils import read_assistants

load_dotenv() # bring in env variables
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"] # assign api key to constant var
STORYTELLERS = read_assistants()

class DataManager:
    """Manages Data communication"""
    def __init__(self, data = None):
        if data is not None:
            self.data = data

        else: # provide structure to avoid errors
            self.data = get_specified_user("test")

    def __str__(self):
        print("Accessing data", self.data)
        current_user = "User: ${self.data.user}\n"
        current_runtime = "Runtime: ${self.data.runtime}\n"
        current_conversation = "Conversation:\n${conversation}\n"
        return current_user + current_runtime + current_conversation

    def set_data(self, user_name: str):
        """ Sets data based on 'user_name' """
        users = read_users()
        print(f"Updating Data from {self.data}...\n")
        try:
            print("username", user_name)
            self.data = users[user_name]
            print(f"Successfully updated Data to {self.data}")
            return True
        except KeyError:
            return False

    def create_user(self, user_name: str, assistant: str) -> None:
        """Creates User within 'users.json' as dict"""

        users_path = Path(__file__).parent.parent / "json" / "users.json"

        new_data = {
            user_name: {
                "name": user_name,
                "age": 6,
                "voice": "nova",
                "assistant": assistant,
                "stories": {}
            }
        }

        data = read_users()
        data.update(new_data)
        print(data)

        with open(users_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

    def save_conversation(self, new_line: list) -> bool:
        """ Appends newLine to data.conversation Array """
        length = len(self.data.conversation)
        self.data.conversation.append(new_line)
        print("Current Conversation: ", self.data.conversation)

        if len(self.data.conversation) == length:
            return False # session failed to update
        return True # session successfully updated

    def get_conversation(self, latest = 0) -> list:
        """ Returns Entire or a Segment of the Conversation """
        # no param returns entire conversation
        if latest == 0:
            return self.data.conversation
    
        # param returns segments of conversation
        requested = []
        for x in range(1, latest):
            requested.append(self.data.conversation[-x])
        return requested

    def manage_threads(self, action, thread: str = None, content: str = None):
        """ Handles CRUD actions for OpenAI thread objs """
        client = OpenAI(api_key=OPENAI_API_KEY) # initialize client

        if action == "CREATE": # create new thread
            thread = client.beta.threads.create()
            return thread.id
        if action == "READ" & thread != None: # retrieve an existing thread
            thread = client.beta.threads.retrieve(
                thread_id = thread
            )
            return thread
        if action == "UPDATE" & thread != None: # update an existing thread
            run = client.beta.threads.runs.create(
                thread_id = thread,
                assistant_id = self.data.assistant
            )

            while run.status == "queued" or run.status == "in_progress":
                run = client.beta.threads.runs.retrieve(
                    thread_id=thread.id,
                    run_id=run.id,
                )
                time.sleep(0.15)

            messages = client.beta.threads.messages.list(
                thread_id = thread
            )
            for message in reversed(messages.data):
                print(message.role + " : " + message.content[0].text.value)

            return messages
        if action == "DELETE" & content != None: # delete an existing thread
            thread = client.beta.threads.delete(
                thread_id = thread
            )
            return thread

        # no condition triggers -> return None
        print("Invalid action, No action taken")
        return None
