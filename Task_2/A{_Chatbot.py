def chatbot():
    print("Welcome to the chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "hello":
            print("Chatbot: Hello there!")
        elif user_input.lower() == "how are you":
            print("Chatbot: I'm doing well, thanks!")
        elif user_input.lower() == "what's your name":
            print("Chatbot: My name is Chatbot.")
        elif user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I didn't understand that.")

chatbot()