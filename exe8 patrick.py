# https://campus.datacamp.com/courses/building-chatbots-in-python/chatbots-101?ex=11
# Now you're going to put everything from the previous exercises together and experience the magic!
# The match_rule(), send_message(), and replace_pronouns() functions have already been defined,
# and the rules dictionary is available in your workspace.
# Your job here is to write a function called respond() with a single argument message which creates an
# appropriate response to be handled by send_message().

# Instructions
# 1. Get a response and phrase by calling match_rule() with the rules dictionary and message.
# 2. Check if the response is a template by seeing if it includes the string '{0}'. If it does: Use the replace_pronouns() function on phrase.
# 3. Include the phrase by using .format() on response and overriding the value of response.
# 4. Hit 'Submit Answer' to see how the bot responds to the provided messages!

import re
import random

bot_template = "BOT : {0}"
user_template = "USER : {0}"

rules = {'I want (.*)': ['What would it mean if you got {0}',
                         'Why do you want {0}',
                         "What's stopping you from getting {0}"],
         'do you remember (.*)': ['Did you think I would forget {0}',
                                  "Why haven't you been able to forget {0}",
                                  'What about {0}',
                                  'Yes .. and?'],
         'do you think (.*)': ['if {0}? Absolutely.', 'No chance'],
         'if (.*)': ["Do you really think it's likely that {0}",
                     'Do you wish that {0}',
                     'What do you think about {0}',
                     'Really--if {0}']
         }


# Define match_rule()
def match_rule(rules, message):
    response, phrase = "default", None

    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.search(pattern, message)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
    # Return the response and phrase
    return response, phrase


# Define replace_pronouns()
def replace_pronouns(message):

    message = message.lower()
    if 'me' in message:
        # Replace 'me' with 'you'
        return re.sub('me', 'you', message)
    if 'my' in message:
        # Replace 'my' with 'your'
        return re.sub('my', 'your', message)
    if 'your' in message:
        # Replace 'your' with 'my'
        return re.sub('your', 'my', message)
    if 'you' in message:
        # Replace 'you' with 'me'
        return re.sub('you', 'me', message)

    return message

# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))

# Define respond()
def respond(message):
    # Call match_rule
    response, phrase = match_rule(rules,message)
    if '{0}' in response:
        # Replace the pronouns in the phrase
        phrase = replace_pronouns(phrase)
        # Include the phrase in the response
        response = response.format(phrase)
    return response

# Send the messages
send_message("do you remember your last birthday")
send_message("do you think humans should be worried about AI")
send_message("I want a robot friend")
send_message("what if you could be anything you wanted")
