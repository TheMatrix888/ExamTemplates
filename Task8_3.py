from itertools import product

n = 0
for number in product("0123456789ABCDEF", repeat=5):
    if number[0] == "0":
        pass
    digits_found = 0
    for digit in number:
        if digit in "0123456789":
            digits_found += 1
    if digits_found == 1:
        n += 1

print(n)
