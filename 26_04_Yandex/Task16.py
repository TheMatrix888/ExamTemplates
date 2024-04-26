a = [1]*13
for n in range(13, 2025):
    a.append(a[n-1]+n-2)

print(a[2024]-a[2020])