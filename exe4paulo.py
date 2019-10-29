# https://campus.datacamp.com/courses/building-chatbots-in-python/chatbots-101?ex=6
# Adding variety
# It can get a little boring hearing the same old answers over and over. In this exercise, you'll add some variation.
# If you ask your bot how it's feeling, the likelihood that it responds with "oh I'm great!" or "I'm very sad today" should be equal.
# Here, you'll use the random module - specifically random.choice(ls) - which randomly selects an element from a list ls.
# A dictionary called responses, which maps each message to a list of possible responses, has been defined for you.

# Instructions 1
# Import the random module.
# If the message is in responses, use random.choice() in the respond() function to choose a random matching response.
# If the message is not in responses, choose a random default response.


# Import the random module
import random

# Create templates
bot_template = "BOT : {0}"
user_template = "USER : {0}"

name = "Greg"
weather = "cloudy"

# Define a dictionary containing a list of responses for each message
responses = {
  "what's your name?": [
      "my name is {0}".format(name),
      "they call me {0}".format(name),
      "I go by {0}".format(name)
   ],
  "what's today's weather?": [
      "the weather is {0}".format(weather),
      "it's {0} today".format(weather)
    ],
  "default": ["default message"]
}

# Use random.choice() to choose a matching response
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return a random matching response
        bot_message = random.choice(responses[message])
    else:
        # Return a random "default" response
        bot_message = random.choice(responses["default"])
    return bot_message


# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))


send_message("what's your name?")
send_message("what's your name?")
send_message("what's your name?")