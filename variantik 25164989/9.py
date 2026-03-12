f = open(r"9.txt")
data = [[int(i) for i in row.split()] for row in f]

def check(row: list):
    row = sorted(row)
    return len(row) == len(set(row)) and (row[0] + row[-1]) * 2 == sum(row[1:-1])


k = 0
for row in data:
    if check(row):
        k += 1
print(k)