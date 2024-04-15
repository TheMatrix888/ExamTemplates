res = []
for N in range(1, 1000000):
    # print(N)
    B = bin(N)[2:]
    # print(B)
    B = B + B[-1]
    # print(B)
    B = B + str(B.count('1')%2)
    # print(B)
    R = int(B, 2)
    # print(R)
    res.append(R)
print(max([x for x in res if x < 13500]))
