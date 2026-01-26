f = open(r"C:\Users\Misha\AppData\Local\Education\PythonProject\Ege\homework variantik 25093318\17_21416.txt")

data = [int(i) for i in f]
summa_otr = 0
for i in data:
    if i < 0:
        summa_otr += i
def check(troika: list):
    sorted_troika = sorted(troika)
    proizv = sorted_troika[0] * sorted_troika[-1]
    return proizv > summa_otr


spisok = []
k = 0
for i in range(len(data) - 2):
    troika = data[i:i+3]
    if check(troika):
        k += 1
        spisok.append(sum(troika))
print(k, max(spisok))