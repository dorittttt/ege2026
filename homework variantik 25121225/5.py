spisok = []
for n in range(1, 10000):
    bin_n = bin(n)[2:]
    if n % 4 == 0:
        bin_n += bin_n[-2:]
    else:
        bin_n += bin(n % 4)[2:]
    r = int(bin_n, 2)
    if r > 250:
        spisok.append(r)
print(min(spisok))