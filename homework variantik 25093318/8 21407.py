from itertools import product
alf = "ДГИАШЭ"
k = 0
for letter in product(sorted(alf), repeat =5):
    word = "".join(letter)
    if word[0] not in ("ИАЭ") and word[-1] not in ("ДГШ"):
        k += 1
        print(word)
print(k)