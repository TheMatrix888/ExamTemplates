res = []
for x in range(22):
    for y in range(22):
        X = (((((3*22+4)*22+2)*22+5)*22+6)*22+x)*22+4
        Y = (((((7*22+2)*22+8)*22+4)*22+7)*22+y)*22+3
        sum = X + Y
        if sum % 125 == 0:
            res.append(sum)
print(max(res))