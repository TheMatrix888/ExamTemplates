from itertools import product
ignore = False
n = 1
consonants = "ПРВЧК"
for combination in product(sorted("ПРИВЫЧКА"), repeat=5):
    word = ''.join(combination)
    print(n, word)
    if n % 5 == 0 and not ignore:
        ignore = True
        continue
    ignore = False
    flag = True
    for letter in word:
        if (not (letter in consonants)) or (len(set(word)) != 5):
            flag = False
            break
    if flag:
        print(n, word)
        break
    n += 1

# TODO answer incorrect, check kege
