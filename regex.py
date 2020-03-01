import re

# The english wordlist ASCII file
file = "data/words_alpha.txt"

# Variables
total = 5            # Total of letters the word must contain
letters = "tiayevr"       # All the letters available. Is not necessary to repeat letters

# Dict() to provide letters already discovered.
#   key: position of the letter in the word
#   value: the letter

fixed = {

}

# Using loop to create regular expression
pattern = ""
for l in range(1, total+1):
    if l in fixed:
        pattern += "[" + fixed[l] + "]"
    else:
        pattern += "[" + letters + "]"

pattern = "^" + pattern + "$"

# Tupple containing each letter.
# It's necessary to use it with startswith(), since doesn't allowed regex, neither list()
initial = tuple(i for i in list(letters))

# Hello wordlist
wordlist = open(file, "r")
for word in wordlist:

    # Check if the word starts with any letter in the tuple (initial)
    if word.startswith(initial):

        for i in letters:
            if letters.count(i) != word.count(i):
                # print(f"{i} -> {letters.count(i)}")
                break
            else:

                # Validate if the regular expression match the word we just read
                result = re.match(pattern, word)
                if result:
                    print(result[0])

# Goodby wordlist
wordlist.close()
