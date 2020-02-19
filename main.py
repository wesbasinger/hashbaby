import itertools
import hashlib
from Crypto.Hash import MD2

def hash(combo):

	first_pass = hashlib.sha1()

	first_pass.update(b'combo')

	sha1_hashed = first_pass.digest()

	second_pass = MD2.new()

	second_pass.update(sha1_hashed)

	md2_hashed = second_pass.digest()

	third_pass = hashlib.md5()

	third_pass.update(md2_hashed)

	return third_pass.hexdigest()

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

combos = itertools.product(letters, repeat=6)

i = 0
'''
for combo in combos:

	if hash("".join(combo)) == "e24b02c81cabe0d4af45f9ceaccde2c7":

		print("The cracked text is ... " + "".join(combo))

		break

	else:

		i += 1

	if i % 100000000 == 0:

		print("Gone through " + str(i) + " iterations.")
'''

print(hash("aaaaaa"))
