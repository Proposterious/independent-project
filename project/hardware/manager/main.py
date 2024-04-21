# Import necessary modules
import sys
import asyncio
from data_manager import DataManager
from conversation_manager import ConversationManager

# runs on startup
async def main():
    """Initialize scripts, classes, hardware"""
    data_manager = DataManager()
    conversation_manager = ConversationManager(assistant="asst_tHhDGtl8tSJIVTrMd95yt9Uk")
  
    # Grab User Info
    user_exists = await conversation_manager.introduce_user()
    print("user_exists", user_exists)
    if user_exists is True:
        # Attempt to retrieve and update user data
        user_name = await conversation_manager.get_name()
        if bool(data_manager.set_data(user_name)) is True:
            return "complete"
    elif user_exists is False: # in-progress
       conversation_manager.new_user()
    else:
        print("Could not determine if user exists, ", user_exists)
        sys.exit()

# runs after setup
async def loop():
    """Serves as repetitive interaction loop"""
    print("blah")
# # Entry point of the application
# if __name__ == "__main__":
#     main()
asyncio.run(main())
asyncio.run(loop())