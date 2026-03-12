from string import digits, ascii_uppercase
alf = digits + ascii_uppercase[:22 - 10]

for x in alf:
    num = int("12313" + x + "57", 22) + int("1" + x + "34561", 22)
    if num % 21 == 0:
        print(x, num // 21)