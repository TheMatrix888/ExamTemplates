from itertools import product, permutations


def f(x, y, z, w):
    return (x and y) or ((z == y) and w)


for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat = 7):
    table = [
        (a1, a2, 1, 1),
        (a3, 0, 0, a4),
        (a5, 0, a6, 0),
        (a7, 0, 0, 0)
    ]
    if len(table) == len(set(table)):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p, row))) for row in table] == [0, 0, 1, 1]:
                print(*p, sep="")
