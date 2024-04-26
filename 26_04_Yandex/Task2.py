from itertools import product, permutations


def f(k, l, m, n):
    return not n or k and not m or (l==m)


for a1, a2, a3, a4 in product([0, 1], repeat = 4):
    table = [
        [0, 1, 0, a1],
        [a2, 0, 0, a3],
        [1, 0, a4, 1]
    ]
    if table[0] == table[1] or table[1] == table[2] or table[0] == table[2]:
        continue
    for p in permutations("klmn"):
        if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
            print(*p, '\n', table, sep='',)
