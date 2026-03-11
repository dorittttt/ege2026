def f(start, stop):
    if start == stop:
        return True
    if start > stop:
        return False
    return sum([f(start + 2, stop), f(start + 3, stop), f(start * 2, stop)])
print(f(10, 30) * f(30, 40))