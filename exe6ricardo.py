# https://campus.datacamp.com/courses/building-chatbots-in-python/chatbots-101?ex=9

# ELIZA II: Extracting key phrases
# The really clever thing about ELIZA is the way the program appears to understand what you told it by occasionally
# including phrases uttered by the user in its responses.
# In this exercise, you will match messages against some common patterns and extract phrases using re.search().
# A dictionary called rules has already been defined, which matches the following patterns:
#     "do you think (.*)"
#     "do you remember (.*)"
#     "I want (.*)"
#     "if (.*)"

# Inspect this dictionary in the Shell before starting the exercise.

# Instructions

# Iterate over the rules dictionary using its .items() method, with pattern and responses as your iterator variables.
# Use re.search() with the pattern and message to create a match object.
# If there is a match, use random.choice() to pick a response.
# If '{0}' is in that response, use the match object's .group() method with index 1 to retrieve a phrase.

import re
import random

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
    return response.format(phrase)


# Test match_rule
print(match_rule(rules, "do you remember your last birthday"))
