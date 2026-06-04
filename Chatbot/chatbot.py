print("Customer Service Chatbot")
print("Type 'bye' to exit")

while True:
    user = input("You: ").lower()

    if user == "hi":
        print("Bot: Hello! How can I help you?")

    elif user == "what is ai":
        print("Bot: AI means Artificial Intelligence.")

    elif user == "internship":
        print("Bot: Internship details are available on our portal.")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")