"""DataManager Class"""
from utils.file_utils import read_users
class DataManager:
    """Manages Data communication"""
    def __init__(self, data = None):
        if data is not None:
            self.data = data

        else: # provide structure to avoid errors
            self.data = {
                "user": "None",
                "runtime": "N/A",
                "conversation": []
            }

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
            self.data = users[user_name]
            print(f"Successfully updated Data to {self.data}")
            return True
        except KeyError:
            return False
        
    def save_conversation(self, new_line: list) -> bool:
        """ Appends newLine to data.conversation Array """

        length = len(self.data.conversation)
        self.data.conversation.append(new_line)
        print("Current Conversation: ", self.data.conversation)

        if len(self.data.conversation) == length:
            return False # session failed to update
        return True # session successfully updated

    def get_conversation(self, latest = 0) -> list:
        """Returns Entire or a Segment of the Conversation"""
        # no param returns entire conversation
        if latest == 0:
            return self.data.conversation
        # param returns segments of conversation
        requested = []
        for x in range(1, latest):
            requested.append(self.data.conversation[-x])
        return requested

