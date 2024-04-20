def del_func(n, m):
    return n % m == 0


for A in range(1, 500):
    flag = True
    for x in range(1, 1000000):
        f = not (del_func(x, 72)) or del_func(x, 495) or not (del_func(x, A))
        if not f:
            flag = False
            break
    if flag:
        print(A)
        break
