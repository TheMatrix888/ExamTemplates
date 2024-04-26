with open("Task17.txt") as file:
    s = [int(x) for x in file]

max21 = max([x for x in s if x % 21 == 0])

res = []
for i in range(len(s)-1):
    a = s[i]
    b = s[i+1]
    if a > max21 or b > max21:
        res.append(a+b)

print(len(res), min(res))