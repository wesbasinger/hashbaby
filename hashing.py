from Crypto.Hash import MD2
import hashlib

f = open("six-letter-words.txt")

configs = []

for i in range(1, 64):

    configs.append(f'{i:06b}')

def mixup(word):

    combos = []

    for config in configs:

        result = ""

        for i in range(6):

            if config[i] == "1":

                result += word[i].upper()

            else:

                result += word[i]

        combos.append(result)

    return combos

def hash(text):

    bin_text = bytes(text, "ascii")

    sha1 = hashlib.sha1(bin_text)
    first = sha1.digest()

    md2 = MD2.new()
    md2.update(first)
    second = md2.digest()

    md5 = hashlib.md5()
    md5.update(second)

    return md5.hexdigest()

for word in f.read().splitlines():

    combos = mixup(word)

    for combo in combos:

        if hash(combo) == "e24b02c81cabe0d4af45f9ceaccde2c7":

            print("SOLUTION is..." + combo)
