from itertools import product

n = 1
for p in product(sorted("ПАРУС"), repeat=5):
    word = "".join(p)
    if word.count("У") <= 1 and "АА" not in word:
        print(n, word)
    n += 1