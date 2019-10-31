# https://campus.datacamp.com/courses/building-chatbots-in-python/chatbots-101?ex=10
# ELIZA III: Pronouns

# To make responses grammatically coherent, you'll want to transform the extracted phrases from first to second
# person and vice versa. In English, conjugating verbs is easy, and simply swapping "me" and 'you',
# "my" and "your" works in most cases.

# In this exercise, you'll define a function called replace_pronouns() which uses re.sub()
# to map "me" and "my" to "you" and "your" (and vice versa) in a string.

# Instructions

# If 'me' is in message, use re.sub() to replace it with 'you'.
# If 'my' is in message, replace it with 'your'.
# If 'your' is in message, replace it with 'my'.
# If 'you' is in message, replace it with 'me'.
import re

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

print(replace_pronouns("my last birthday"))
print(replace_pronouns("when you went to Florida"))
print(replace_pronouns("I had my own castle"))
