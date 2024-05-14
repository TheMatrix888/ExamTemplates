def f(a, b, turn):
    if a + b <= 20:
        return turn % 2 == 0
    if turn == 0:
        return 0
    h = [f(a-1, b, turn-1), f(a, b-1, turn-1), f((a+1)//2, b, turn-1), f(a, (b+1)//2, turn-1)]
    if (turn-1) % 2 == 0:
        return any(h)
    else:
        return all(h)


print("19 >>> ", [s for s in range(11, 100) if f(10, s, 2)])
print("20 >>> ", [s for s in range(11, 100) if not f(10, s, 1) and f(10, s, 3)])
print("21 >>> ", [s for s in range(11, 100) if not f(10, s, 2) and f(10, s, 4)])