from itertools import product, permutations

def f(x, y, w, u):
    return (not((not y or w) == x)) and u

for a1, a2, a3 in product([0, 1], repeat=3):
    table = [
        (0, 1, 0, a1),
        (0, 1, 1, 1),
        (1, 0, 1, a2),
        (1, a3, 1, 1)
    ]
    if len(table) == len(set(table)):
        for p in permutations("xywu"):
            if [f(**dict(zip(p, row))) for row in table] == [0, 0, 1, 1]:
                print(*p, sep='')
