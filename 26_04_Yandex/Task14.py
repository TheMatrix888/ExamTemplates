def to_29(number, value):
    res = 0
    for digit in number:
        res *= 29
        if digit == "x":
           res += value
        else:
            res += int(digit)
    return res


for x in range(29):
    Sum = to_29("42x158", x) + to_29("16x234", x)
    if Sum % 28 == 0:
        print(Sum/28)
        break