with open("Task27_B.txt") as file:
    n = int(file.readline())
    val = [int(x) for x in file]
mxcount = 0
count = 1
k = 263
summ = 0
for i in range(n-1):
    summ = val[i]
    count = 1
    for j in range(i+1, n):
        summ += val[j]
        count += 1
        if summ % k == 0:
            mxcount = max(count, mxcount)
print(mxcount)
