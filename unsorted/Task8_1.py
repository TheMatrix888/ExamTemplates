from itertools import product
alphabet = "0123456789ABCD"
n = 0
for number in product(alphabet, repeat=5):
    if (number[0] != "0") and (len(set(number)) == 2) and ((number[-1] == "0") or (number[-1] == "3")):
        n += 1
print(n)
