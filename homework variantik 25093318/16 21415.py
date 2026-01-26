from functools import lru_cache

@lru_cache(None)
def f(n):
    if n <= 5:
        return 1
    if n > 5:
        return n + f(n - 2)

for i in range(1, 1000):
    f(i)

print(f(2126) - f(2122))