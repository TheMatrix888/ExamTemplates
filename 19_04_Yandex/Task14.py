def to_22(number, value):
    res = 0
    for digit in number:
        if digit == 'x':
            res += value
        else:
            res += int(digit)
        res *= 22
    return res // 22


res = []
for x in range(22):
    for y in range(22):
        X = to_22("34256x4", x)
        Y = to_22("72847x3", y)
        Sum = X+Y
        if Sum % 125 == 0:
            res.append(Sum//125)

print(max(res))