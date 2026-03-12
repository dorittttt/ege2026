from fnmatch import fnmatch

for i in range(0, 10**8, 271):
    if fnmatch(str(i), "12??15*6"):
        print(i, i // 271)