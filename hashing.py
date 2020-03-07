from Crypto.Hash import MD2
import hashlib

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

sphinxi = mixup("sphinx")

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

for combo in mixup("sphinx"):

    print(hash(combo))
