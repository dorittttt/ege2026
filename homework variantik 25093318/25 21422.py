def delit(num):
    spisok = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            spisok.append(i)
            spisok.append(num // i)
    return spisok
k = 0
for i in range(1_125_000 + 1, 100**100):
    spisok2 = []
    for j in delit(i):
        if (str(j)[-1] == "7") and (j != i) and (j != 7):
            spisok2.append(j)
    if k < 5 and spisok2:
        print(i, min(spisok2))
        k += 1
