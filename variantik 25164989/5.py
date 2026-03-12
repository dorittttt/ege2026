spisok = []
for n in range(1, 10000):
    bin_n = bin(n)[2:]
    if n % 2 == 0:
        bin_n = "10" + bin_n
    elif n % 2 != 0:
        bin_n = "1" + bin_n + "01"
    r = int(bin_n, 2)
    if n > 18:
        spisok.append(r)
print(min(spisok))