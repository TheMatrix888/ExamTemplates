from itertools import product, permutations


def list_repeats(l):
    buffer = []
    for element in l:
        if element in buffer:
            return True
        else:
            buffer.append(element)
    return False


def f(x, y, w):
    return (x and (not(w) or y)) == 1


for a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16 in product([0, 1], repeat=16):
    table = [
        [a1, 0, a2],
        [a3, a4, 0],
        [a5, 0, a6],
        [a7, 0, a8],
        [a9, 0, a10],
        [a11, 1, a12],
        [a13, a14, 1],
        [a15, 1, a16]
    ]
    if not list_repeats(table):
        for p in permutations("xyw", r=3):
            if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0, 0, 0, 1, 1, 1]:
                print(*p, sep='')
                print(table)
