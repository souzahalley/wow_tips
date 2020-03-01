
letters = "raten"
file = "data/words_alpha.txt"

with open(file, "r") as line:
    f = line.read()
    wordlist = f.splitlines()


def compare(word, valids = wordlist):
    if word in valids:
        print(f"Found: {word}")

def permutation(word, loop = 0):

    if loop == len(word):
        final = "".join(word)
        compare(final)
        # print(final)

    for i in range(loop, len(word)):
        
        var = list(word)
        var[loop], var[i] = var[i], var[loop]
        
        permutation(var, loop + 1)
    

permutation(letters)




