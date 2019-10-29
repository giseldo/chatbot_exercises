# https://campus.datacamp.com/courses/building-chatbots-in-python/chatbots-101?ex=7

# ELIZA I: asking questions
# Asking questions is a great way to create an engaging conversation. Here, you'll create the very first
# hint of ELIZA's famous personality, by responding to statements with a question and responding to questions with answers.
# A dictionary of responses with "question" and "statement" as keys and lists of appropriate responses as values
# has already been defined for you. Explore this in the Shell with responses.keys() and responses["question"].

# Instructions
# Define a respond() function which takes in message as an argument, and uses the string's .endswith()
# method to check if a message ends with a question mark.
# If the message does end with a question mark, choose a random "question" from the responses dictionary.
# Else, choose a random "statement" from the responses.
# Send the bot multiple messages with and without a question mark - these have been provided for you.
# If you want to experiment further in the Shell, be sure to first hit 'Run Code'.

import random


bot_template = "BOT : {0}"
user_template = "USER : {0}"

responses = {   'question': ["I don't know :(", 'you tell me!'],
                'statement': ['tell me more!',
                            'why do you think that?',
                            'how long have you felt this way?',
                            'I find that extremely interesting',
                            'can you back that up?',
                            'oh wow!',
                            ':)']
             }


def respond(message):
    # Check for a question mark
    if message.endswith("?"):
        # Return a random question
        return random.choice(responses["question"])
    # Return a random statement
    return random.choice(responses["statement"])


# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))



# Send messages ending in a question mark
send_message("what's today's weather?")
send_message("what's today's weather?")

# Send messages which don't end with a question mark
send_message("I love building chatbots")
send_message("I love building chatbots")
