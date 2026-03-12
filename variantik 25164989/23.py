def f(start, stop):
    if start == stop:
        return True
    if start < stop:
        return False
    return sum([
        f(start - 1, stop), f(start // 2, stop)
    ])
print(f(40, 16) * f(16, 6))