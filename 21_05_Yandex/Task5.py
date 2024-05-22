def to_three(n):
    res = ""
    while n:
        res = str(n % 3) + res
        n //= 3
    return res


def sum_digits(n):
    res = 0
    for digit in n:
        res += int(digit)
    return res


res = []
res1 = []
for i in range(10000):
    N = to_three(i)
    if sum_digits(N) % 2 == 0:
        N = N + "0"
        N = "2" + N[2:]
    else:
        N = N + "1"
        N = "20" + N[2:]
    R = int(N, 3)
    if R > 75:
        res.append(i)
        res1.append(R)

print(res[res1.index(min(res1))])