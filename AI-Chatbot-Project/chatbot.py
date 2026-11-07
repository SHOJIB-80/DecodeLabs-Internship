
# Project 1: Rule-Based AI Chatbot
# DecodeLabs Artificial Intelligence Internship

responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there! Nice to meet you!",
    "how are you": "I'm doing great! Thanks for asking.",
    "what is your name": "My name is DecodeBot.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "who created you": "I was created as a DecodeLabs project.",
    "help": "You can ask my name, ask about AI, or say hello.",
    "thank you": "You're welcome!"
}

print("================================")
print("   Welcome to DecodeBot!")
print("================================")
print("Type 'exit' to end the chat.")

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "exit":
        print("Bot: Goodbye! Have a great day!")
        break

    elif user_input in responses:
        print("Bot:", responses.get(user_input))

    else:
        print("Bot: Sorry, I don't understand that.")
