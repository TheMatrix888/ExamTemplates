with open("Task17_1.txt") as file:
    s = [int(line) for line in file]

min_pos_two = 99
for number in s:
    if (number > 0) and (len(str(number)) == 2) and (number < min_pos_two):
        min_pos_two = number


min_pos_two = str(min_pos_two)
res = []
for i in range(len(s)-1):
    a = s[i]
    b = s[i+1]
    if not(min_pos_two in str(a)) or not(min_pos_two in str(b)):
        res.append(abs(a-b))

print(len(res), min(res))
