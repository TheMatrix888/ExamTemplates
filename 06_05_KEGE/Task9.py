with open("Task9.txt") as file:
    fours = [list(map(int, line.split())) for line in file]

n = 0
for four in fours:
    max_four = max(four)
    if max_four < sum(four)-max_four:
        sorted_four = sorted(four)
        if sorted_four[0]+sorted_four[3] == sorted_four[1]+sorted_four[2]:
            n += 1

print(n)
