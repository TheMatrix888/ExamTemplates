from itertools import product, permutations
def f1(x, y, z, w):
    return (w == x) and (not y or z)

def f2(x, y, z, w):
    return not (not w or x) or (y == z)

for a1, a2, a3, a4, a5 in product([0, 1], repeat = 5):
    table = [
        [1, a1, 1, 1],
        [a2, 1, 0, 0],
        [a3, 0, 0, a4]
        ]
    for p in permutations("xyzw"):
        if [f1(**dict(zip(p, row))) for row in table] == [1, 1, 0] and \
           [f2(**dict(zip(p, row))) for row in table] == [0, a5, 0]:
            print(*p, sep='')
