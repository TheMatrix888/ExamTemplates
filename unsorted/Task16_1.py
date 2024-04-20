"""
from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(10000)
@lru_cache
def f(n):
    if n <= 1:
        return 1
    elif n % 2 == 0:
        return f(n-1)/3
    else:
        return 6*f(n-1)
print(f(2049)/f(2046))
"""


a = [1, 1]
for n in range(2, 3000):
    if n % 2 == 1:
        a.append(a[n-1]/3)
    else:
        a.append(6*a[n-1])

print(a[2049]/a[2046])

# UNSOLVED
