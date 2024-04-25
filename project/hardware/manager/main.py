# Import necessary modules
import sys
import asyncio
from data_manager import DataManager
from conversation_manager import ConversationManager

data_manager = DataManager() # initialize DataManager class
conversation_manager = ConversationManager(assistant="asst_tHhDGtl8tSJIVTrMd95yt9Uk") # initialize ConversationManager class

def loop(thread) -> None:
    """Serves as repetitive interaction loop"""
    while True:
        user_input = conversation_manager.user_response()
        response = conversation_manager.assistant_response(user_input, thread)
        print(response)

def options(user_name: str) -> None:
    """Accesses and edits user options"""
    print(user_name)

async def main() -> None:
    """Initializes the program"""
    user_exists: bool = await conversation_manager.introduce_user()
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
        user_name = await conversation_manager.new_user()
        data_manager.create_user(user_name)
        if bool(data_manager.set_data(user_name)) is True:
            print("Updated session")
        else:
            print("Failed to update session")
            sys.exit()
    else:
        print("Could not determine if user exists, ", user_exists)
        sys.exit()

    # Send user into loop or options
    begin_session = await conversation_manager.begin_session()
    if bool(begin_session == "yes"):
        if user_exists is True:
            prev_stories = data_manager.data.stories
            story_index: int = conversation_manager.prev_sessions(prev_stories)

            thread: str = prev_stories[story_index].thread_id
            asyncio.run(loop(thread))
    else:
        asyncio.run(options(data_manager.data.name))
        # ask user if they would like to begin session

# Entry point of the application
if __name__ == "__main__":
    asyncio.run(main())
