# Import necessary modules
import sys
import asyncio
from utils.text_utils import trigger_exit
from utils.file_utils import read_assistants
from data_manager import DataManager
from conversation_manager import ConversationManager

STORYTELLERS = read_assistants()
DEFAULT_STORYTELLER = STORYTELLERS["Limited"]
data_manager = DataManager() # initialize DataManager class
conversation_manager = ConversationManager(assistant=DEFAULT_STORYTELLER) # initialize ConversationManager class

def loop(thread = None) -> None:
    """Serves as repetitive interaction loop"""
    if thread is None:
        thread = data_manager.manage_threads("CREATE")
        conversation_manager.embark(thread)
    else:
        print("this should provide the user a summary of prev thread/story")
    while True:
        user_input = conversation_manager.user_response()
        if trigger_exit(user_input):
            print(conversation_manager.end_communications(thread))
            break

        response = conversation_manager.assistant_response(user_input, thread)
        print(response)

def options() -> None:
    """Accesses and edits user options"""
    # ask user for their name
    user_name = conversation_manager.new_user()
    # assign assistant to user
    assistant = conversation_manager.set_assistant()
    if assistant == "leading":
        data_manager.create_user(user_name, STORYTELLERS["Leading"])
    else:
        data_manager.create_user(user_name, STORYTELLERS["Limited"])

def main() -> None:
    """Initializes the program"""
    user_exists: bool = conversation_manager.introduce_user()
    # Create or find user then update session
    if user_exists is True:
        # Attempt to retrieve and update user data
        user_name = conversation_manager.get_name()
        if bool(data_manager.set_data(user_name)) is True:
            print("Updated session")
        else:
            print("Failed to update session")
            sys.exit()
    elif user_exists is False: # in-progress
        # set up user options
        asyncio.run(options())

        if bool(data_manager.set_data(user_name)) is True:
            print("Updated session")
        else:
            print("Failed to update session")
            sys.exit()
    else:
        print("Could not determine if user exists, ", user_exists)
        sys.exit()

    # Send user into loop or options
    begin_session = conversation_manager.begin_session()
    if begin_session == "yes":
        if user_exists is True:
            prev_stories = data_manager.data['stories']
            story_index: int = conversation_manager.prev_sessions(prev_stories)

            thread: str = prev_stories[story_index].thread_id
            conversation_manager.begin_communications(thread)
            asyncio.run(loop(thread))
        else: # user_exists is False
            asyncio.run(loop())
    else: # send user into options
        asyncio.run(options())
        sys.exit()

# Entry point of the application
if __name__ == "__main__":
    asyncio.run(main())
