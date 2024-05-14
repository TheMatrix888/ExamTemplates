def game(x, y, turn):
    if x + y >= 150:
        return turn % 2 == 1
    if turn == 0:
        return turn % 2 == 0
    h = [game(x+2, y, turn-1), game(x*3, y, turn-1), game(x, y+2, turn-1), game(x, y*3, turn-1)]
    if turn % 2 == 0:
        # Поля
        return all(h)
    else:
        # Вика
        return any(h)

print("19 >>> ", [s for s in range(1, 133+1) if not game(16, s, 2)])
