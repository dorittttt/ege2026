from string import digits, ascii_uppercase

alf = digits + ascii_uppercase[:11]

for x in alf:
    num = int("82934" + x + "2", 21) + int("2924" + x + x + "7", 21) + int("67564" + x + "8", 21)
    if num % 20 == 0:
        print(x, num // 20)