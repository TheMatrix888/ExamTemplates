def f(s, turn):
    if s > 112:
        return (turn-1) % 2 == 0
    if s >= 45:
        return turn % 2 == 0
    if turn == 0:
        return 0
    h = [f(s+2, turn-1), f(s*3, turn-1)]
    if (turn-1) % 2 == 0:
        return any(h)
    else:
        return all(h)


print("19 >>> ", [s for s in range(1, 44+1) if f(s, 2)])