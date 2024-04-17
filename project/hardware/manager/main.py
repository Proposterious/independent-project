# Import necessary modules
from data_manager import DataManager
from conversation_manager import ConversationManager

# Main function
def main():
    """Initialize scripts, classes, hardware"""
    # Initialize classes
    conversation_manager = ConversationManager()
    data_manager = DataManager()

    # Main loop for the conversation
    while True:
        # Get user input
        user_input = input("You: ")

        # Send user input to conversation manager
        response = conversation_manager.respond(user_input)

        # Display response
        print("Bot:", response)

        new_message = [
            {"role": "user", "content": user_input},
            {"role": "system", "content": response}
        ]
        # Store conversation history
        data_manager.save_conversation(new_message)

# Entry point of the application
if __name__ == "__main__":
    main()
