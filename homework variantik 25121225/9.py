f = open(r"9.txt")
data = [[int(i) for i in row.split()] for row in f]

def check(row):
    uniq = [int(i) for i in row if row.count(i) == 1]
    dvazd = [int(i) for i in row if row.count(i) == 2]
    return len(dvazd) == 4 and len(uniq) == 3 and ((sum(dvazd) / len(dvazd)) <= min(uniq))


k = 0
spisok = []
for row in data:
    k += 1
    if check(row):
        k1 = 1
        for i in row:
            k1 *= i
        spisok.append([k, k1])
spisok = sorted(spisok, key=lambda x:(
    -x[0]
))
for i in spisok:
    print(i)