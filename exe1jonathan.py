# https://campus.datacamp.com/courses/building-chatbots-in-python/

# EchoBot I
# Hello, World!
# You'll begin learning how to build chatbots in Python by writing two functions to build the simplest bot
# possible: EchoBot. EchoBot just responds by replying with the same message it receives.
# In this exercise, you'll define a function that responds to a user's message. In the next exercise,
# you'll complete EchoBot by writing a function to send a message to the bot.

# Instructions
# Write a function called respond() with a single parameter message which returns the bot's response.
# To do this, concatenate the strings "I can hear you! You said: " and message.
# Store the concatenated strings in bot_message, and return this result.

bot_template = "BOT : {0}"
user_template = "USER : {0}"


# Define a function that responds to a user's message: respond
def respond(message):
    # Concatenate the user's message to the end of a standard bot respone
    bot_message = "I can hear you! You said: " + message
    # Return the result
    return bot_message


# Test function
print(respond("hello!"))
