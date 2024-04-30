for N in range(1, 1000):
    n = bin(N)[2:]
    if N % 2 == 0:
        n = '1'+n+'1'
    else:
        n = n + '10'
    R = int(n, 2)
    if R > 179:
        print(N)
        break
