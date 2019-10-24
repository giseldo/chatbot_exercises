# https://campus.datacamp.com/courses/building-chatbots-in-python/understanding-natural-language?ex=3
# Intent classification with regex II
# With your patterns dictionary created, it's now time to define a function to
# find the intent of a message.
#
# Instructions
# Iterate over the intents and patterns in the patterns dictionary using its .items() method.
# Use the .search() method of pattern to look for keywords in the message.
# If there is a match, return the corresponding intent.
# Call your match_intent() function inside respond() with message as the argument and
# then hit 'Submit Answer' to see how the bot responds to the provided messages.
import re

bot_template = "BOT : {0}"
user_template = "USER : {0}"

keywords = {
    'greet': ['hello', 'hi', 'hey'],
    'goodbye': ['bye', 'farewell'],
    'thankyou': ['thank', 'thx']
}


responses = {
    'default': 'default message',
    'goodbye': 'goodbye for now',
    'greet': 'Hello you! :)',
    'thankyou': 'you are very welcome'
}

# Define a dictionary of patterns
patterns = {}

# Iterate over the keywords dictionary
for intent, keys in keywords.items():
    # Create regular expressions and compile them into pattern objects
    patterns[intent] = re.compile('|'.join(keys))

# Define a function to find the intent of a message
def match_intent(message):
    matched_intent = None
    for intent, pattern in ____:
        # Check if the pattern occurs in the message 
        if ____:
            matched_intent = ____
    return matched_intent

# Define a respond function
def respond(message):
    # Call the match_intent function
    intent = ____
    # Fall back to the default response
    key = "default"
    if intent in responses:
        key = intent
    return responses[key]

# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))

# Send messages
send_message("hello!")
send_message("bye byeee")
send_message("thanks very much!")
