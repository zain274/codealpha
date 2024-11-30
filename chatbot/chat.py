import nltk
from nltk.chat.util import Chat

pairs = [
    ["hello", ["Greetings!", "How can I assist you today?"]],
    ["how are you", ["I'm doing very well, thank you!", "I'm feeling quite good. How about yourself?"]],
    ["what can you do", ["I am capable of answering your questions, providing summaries of factual topics, or crafting creative stories. What would you like to explore?"]],
    ["tell me a joke", ["I tried starting a hot air balloon business, but it never took off!"]],
    ["goodbye", ["Farewell! Have a wonderful day!"]],
    ["what's the weather like", ["The weather today is sunny.", "It's raining outside at the moment.", "The sky is currently overcast.", "It's snowing heavily."] ],
    ["what's your favorite color", ["My favorite color is a serene blue.", "I do not have a preferred color.", "I appreciate all colors equally."]],
    ["give me a riddle", ["I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?"]],
]

def chat(pairs, reflections):
    # Create a chat session
    chatbot = Chat(pairs, reflections)
    print("Welcome to the chatbot! Type 'quit' to exit.")
    while True:
        user_input = input("> ")
        if user_input.lower() == 'quit':
            break
        response = chatbot.respond(user_input)
        if response is None:
            response = "I'm still learning. Could you please rephrase your question?"
        print(response)

# Run the chatbot
reflections = {
    "am": "are",
    "what": "that",
    "can": "could",
    "will": "would",
    "were": "was",
    "just": "",
    "should": "should",
    "may": "might",
    "isn't": "is not",
    "aren't": "are not",
    "wasn't": "was not",
    "weren't": "were not",
    "haven't": "have not",
    "hasn't": "has not",
    "don't": "do not",
    "doesn't": "does not",
    "didn't": "did not",
    "won't": "will not",
    "can't": "cannot",
    "shouldn't": "should not"
}

# Add riddle and answer
riddle = "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?"
answer = "map"

chat(pairs, reflections)

# Ask for riddle answer
user_answer = input("What is the answer to the riddle? ")
if user_answer.lower() == answer.lower():
    print("Correct!")
else:
    print("Incorrect. The answer is:", answer)

# Keep the chatbot running in an interactive environment
while True:
    user_input = input("> ")
    if user_input.lower() == 'quit':
        break
    response = chatbot.respond(user_input)
    if response is None:
        response = "I'm still learning. Could you please rephrase your question?"

        print(response)
