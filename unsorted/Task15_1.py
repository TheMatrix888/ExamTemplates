def DEL(n, m):
    return n % m == 0

for A in range(1, 500):
    flag = True
    for x in range(1, 1000000):
        f = not(DEL(x, 72)) or DEL(x, 495) or not(DEL(x, A))
        if not f:
            flag = False
            break
    if flag:
        print(A)
        break
