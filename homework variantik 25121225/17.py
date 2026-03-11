f = open(r"17_24564.txt")
data = [int(i) for i in f]
min_el = min([int(i) for i in data if 100 <= (i) <= 999])
def check(troika: list):
    k1 = len([int(i) for i in troika if 100 <= abs(i) <= 999])
    return k1 == 1 and sum(troika) % min_el == 0


k = 0
spisok = []
for i in range(len(data) - 2):
    troika = data[i:i+3]
    if check(troika):
        k += 1
        spisok.append(sum(troika))
        print(troika)
print(k, max(spisok))