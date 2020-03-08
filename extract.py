f = open("alpha.txt")

g = open("six-letter-words.txt", "w")

for word in f.read().splitlines():

    if len(word) == 6:

        g.write(word.lower())
        g.write("\n")

g.close()
