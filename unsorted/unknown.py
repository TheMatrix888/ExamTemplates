def transform(equation, base, value):
    result = 0
    for digit in equation:
        result *= base
        if digit == "x" or digit == "y":
            result += value
        else:
            result += int(digit)
    return result


for x in range(15):
    for y in range(17):
        X = transform("123x5", 15, x)
        Y = transform("67y9", 17, y)
        if (X + Y) % 131 == 0:
            print(x, y, (X+Y)//131)