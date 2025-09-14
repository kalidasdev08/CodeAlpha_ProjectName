# Basic Rule-Based Chatbot (with new default response)

def chatbot_response(user_input):
    """Return chatbot response based on user input"""
    user_input = user_input.lower()  # make it case-insensitive
    
    if "hello" in user_input or "hi" in user_input:
        return "Hi! 👋"
    elif "how are you" in user_input:
        return "I'm fine, thanks! How about you?"
    elif "thanks" in user_input or "thank you" in user_input:
        return "You're welcome! 😊"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day! 😊"
    elif "your name" in user_input:
        return "I'm a simple chatbot created by you!"
    else:
        # 🔹 changed the default response here
        return "Hmm... I don't know how to answer that yet. 😅"

print("=== Basic Chatbot ===")
print("Type 'bye' to exit.\n")

# Main loop
while True:
    user_message = input("You: ")
    response = chatbot_response(user_message)
    print("Bot:", response)
    
    if "bye" in user_message.lower() or "goodbye" in user_message.lower():
        break
