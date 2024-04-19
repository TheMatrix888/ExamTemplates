def sum_digits(n):
    Sum = 0
    for digit in str(n):
        Sum += int(digit)
    return Sum


for N in range(1000, 1000000):
    if '0' in str(N):
        continue
    T = sum_digits(N)
    ost = [T % int(digit) for digit in str(N)]
    ost.sort(reverse=True)
    ost = list(map(str, ost))
    R = int(''.join(ost))
    if R > 2000:
        print(N)
        break
