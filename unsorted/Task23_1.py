def f(n, target):
    if n == target:
        return 1
    elif n < target:
        return 0
    else:
        val1 = f(n//3, target)
        if n % 3 != 0:
            val2 = f(n-(n % 3), target)
        else:
            val2 = f(n-1, target)
        return val1 + val2

print(f(58, 3))
