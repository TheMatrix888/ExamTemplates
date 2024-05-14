def f(n, m, turn):
    if n + m >= 45:
        return turn % 2 == 0
    if turn == 0:
        return 0
    h = [f(n+1, m, turn-1), f(n, m+1, turn-1), f(n*3, m, turn-1), f(n, m*3, turn-1)]
    if (turn-1) % 2 == 0:
        return any(h)
    else:
        return all(h)


print("19 >>> ", [s for s in range(1, 41) if f(4, s, 2)])   # all -> any
print("20 >>> ", [s for s in range(1, 41) if not f(4, s, 1) and f(4, s, 3)])
print("21 >>> ", [s for s in range(1, 41) if not f(4, s, 2) and f(4, s, 4)])