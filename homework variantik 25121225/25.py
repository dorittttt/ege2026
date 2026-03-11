def delit(num):
    deliteli = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            deliteli.append(i)
            deliteli.append(num // i)
    if deliteli:
        return (min(deliteli) * max(deliteli)) // 2
    return int(num ** 0.5)

k = 0
for i in range(405_000 + 1, 10**10):
    if delit(i) % 3 == 0:
        print(i, delit(i))
        k += 1
        if k == 5:
            break