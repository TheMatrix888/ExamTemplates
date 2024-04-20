with open("Task24_1.txt") as file:
    s = file.readline()

arr = []
for index, letter in enumerate(s):
    if letter == "A":
        arr.append(index)

res = []
for i, j in zip(arr, arr[2023:]):
    res.append(j - i + 1)

print(min(res))
