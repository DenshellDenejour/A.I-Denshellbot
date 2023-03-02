import random

greetings = ["hello", "hi", "hey", "greetings", "what's up"]
responses = ["hi bitch!", "hello!", "hey!", "nice to meet you nigga!"]


def chatbot():
    user_input = input("User: ")
    if user_input.lower() in greetings:
        response = random.choice(responses)
    else:
        response = "I'm sorry, I don't understand you fucking nigga."
    print("Chatbot: " + response)


while True:
    chatbot()
