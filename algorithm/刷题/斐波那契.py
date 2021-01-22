def fb(n):
    if n == 1 or n == 2:
        return n
    else:
        return fb(n - 1) + fb(n - 2)


print(fb(5))
