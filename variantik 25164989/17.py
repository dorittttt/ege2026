f = open(r"17_27629 (1).txt")
data = [int(i) for i in f]

max_el_4 = max([int(i) for i in data if 1000 <= abs(i) <= 9999 and str(i)[-2:] == "43"]) ** 2


def check(pari: list):
    k1 = len([int(i) for i in pari if 1000 <= abs(i) <= 9999])
    return k1 >= 1 and sum(pari) ** 2 < max_el_4

k = 0
spisok = []
for i in range(len(data) - 1):
    pari = data[i:i+2]
    if check(pari):
        k += 1
        spisok.append(sum(pari) ** 2)
print(k, max(spisok))