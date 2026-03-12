f = open(r"26_27779.txt")
n = int(f.readline())

data = sorted(set(int(i) for i in f), reverse=True)

cake = [data[0]]

for piece in data[1:]:
    if cake[-1] - piece >= 8:
        cake.append(piece)
print(len(cake), cake[-1])