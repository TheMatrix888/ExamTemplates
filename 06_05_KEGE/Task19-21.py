def f(s, m, turn):
    if s >= 84:
        return turn % 2 == 0
    if turn == 0:
        return 0
    h = [f(s + 1, turn - 1)]
    if s % 2 == 0:
        h.append(f(s * 1.5, turn - 1))
    else:
        h.append(f(s * 2, turn - 1))
    if turn % 2 != 0:
        return any(h)
    else:
        return all(h)

print("19 >>> ", [s for s in range(1, 83+1) if f(s, 1 4) - f(s, 1,2)])
