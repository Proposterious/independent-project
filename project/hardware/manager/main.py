# Import necessary modules
import sys
import asyncio
from data_manager import DataManager
from conversation_manager import ConversationManager

"""Initialize scripts, classes, hardware"""
data_manager = DataManager()
conversation_manager = ConversationManager(assistant="asst_tHhDGtl8tSJIVTrMd95yt9Uk")
# runs on startup
async def main():
    # Find or create user
    user_exists = await conversation_manager.introduce_user()
    print("user_exists", user_exists)
    if user_exists is True:
        # Attempt to retrieve and update user data
        user_name = await conversation_manager.get_name()
        if bool(data_manager.set_data(user_name)) is True:
            print("Updated session")
        else:
            print("Failed to update session")
            sys.exit()
    elif user_exists is False: # in-progress
       user_name = await conversation_manager.new_user()
       if bool(data_manager.set_data(user_name)) is True:
            print("Updated session")
       else:
            print("Failed to update session")
            sys.exit()
    else:
        print("Could not determine if user exists, ", user_exists)
        sys.exit()

    # Send user into loop or update settings
    begin_session = await conversation_manager.begin_session()
    if bool(begin_session == "yes"):
        return
    else:
        asyncio.run(options)
        # ask user if they would like to begin session
    
# runs after setup
async def loop():
    """Serves as repetitive interaction loop"""
    print("blah")

async def options(user):
    print("blah")

# # Entry point of the application
# if __name__ == "__main__":
#     main()
asyncio.run(main())
asyncio.run(loop())
