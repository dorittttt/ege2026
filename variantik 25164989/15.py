def delit(n, m):
    return n % m == 0

for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not(
                delit(x, 21) <= ((not(delit(x, a))) <= (not(delit(x, 77))))
        ):
            flag = False
    if flag:
        print(a)