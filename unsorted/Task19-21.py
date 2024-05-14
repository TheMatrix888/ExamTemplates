def f(s, turn):
    if s >= 25:
        return turn % 2 == 0
    if turn == 0:
        return 0
    h = [f(s+2, turn-1), f(s*2, turn-1)]
    if (turn-1) % 2 == 0:
        return any(h)
    else:
        return all(h)



print("19 >>> ", min([s for s in range(1, 24+1) if f(s, 2)]))
print("20 >>> ", len([s for s in range(1, 24+1) if not f(s, 1) and f(s, 3)]))
print("21 >>> ", [s for s in range(1, 24+1) if not f(s,2) and f(s, 4)])