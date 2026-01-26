spisok = []
for n in range(1, 10**5):
    bin_n = bin(n)[2:]
    summa = sum(int(i) for i in bin_n)
    if summa % 2 == 0:
        bin_n = '10' + bin_n[2:] + '0'
    if summa % 2 != 0:
        bin_n = '11' + bin_n[2:] + '1'
    r = int(bin_n, 2)
    if r > 480:
        spisok.append(n)
print(min(spisok))