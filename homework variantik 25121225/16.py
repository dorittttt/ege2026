from sys import setrecursionlimit
setrecursionlimit(30000)

def g(n):
    return f(n - 3)
def f(n):
    if n <= 20:
        return 177
    elif n > 20:
        return g(n - 2) + 4
print(g(22222))