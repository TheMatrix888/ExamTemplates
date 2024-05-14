with open("Task17.txt") as file:
    s = [int(line) for line in file]

third = sorted(s, reverse=True)[2]

res = []
for i in range(len(s)-2):
    a, b, c = s[i], s[i+1], s[i+2]
    counter = 0
    if a % 2 == 0:
        counter += 1
    if b % 2 == 0:
        counter += 1
    if c % 2 == 0:
        counter += 1
    if counter <= 2:
        if a+b+c <= third:
            res.append(a+b+c)

print(len(res), max(res))
