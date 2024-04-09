# Import necessary modules
from conversation_manager import ConversationManager
from data_manager import DataManager

# Main function
def main():
    # Initialize necessary components
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

        # Store conversation history
        data_manager.save_conversation("You: " + user_input, "Bot: " + response)

# Entry point of the application
if __name__ == "__main__":
    main()