f = open(r"C:\Users\Misha\AppData\Local\Education\PythonProject\Ege\homework variantik 25093318\9_21408.txt")
data = [[int(i) for i in row.split()] for row in f]

def check(row):
    uniq = []
    povt_2_3 = []
    for i in row:
        if row.count(i) == 1:
            uniq.append(i)
        if row.count(i) == 3:
            povt_2_3.append(i)
    sorted_povt = sorted(povt_2_3)
    return len(povt_2_3) == 6 and len(uniq) == 1 and sorted_povt[-1] > uniq[0]

k = 0
for row in data:
    if check(row):
        k += 1

print(k)