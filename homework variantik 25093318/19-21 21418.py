# def f(s, step = 1): #p1 v2 p3 v4 p5
#     if s <= 87 and step == 3:
#         return True
#     if (s > 87 and step == 3) or (s <= 87 and step < 3):
#         return False
#
#     moves = [
#         f(s - 2, step + 1),
#         f(s // 2, step + 1)
#     ]
#
#     if step % 2 == 0:
#         return any(moves)
#     return all(moves)
#
# for s in range(88, 10**3):
#     if f(s):
#         print(s)
#
# def f(s, step = 1): #p1 v2 p3 v4 p5
#     if s <= 87 and step == 4:
#         return True
#     if (s > 87 and step == 4) or (s <= 87 and step < 4):
#         return False
#
#     moves = [
#         f(s - 2, step + 1),
#         f(s // 2, step + 1)
#     ]
#
#     if step % 2 != 0:
#         return any(moves)
#     return all(moves)
#
# for s in range(88, 10**3):
#     if f(s):
#         print(s)

def f(s, step = 1): #p1 v2 p3 v4 p5
    if s <= 87 and step == 3:
        return True
    if (s > 87 and step == 3) or (s <= 87 and step < 3):
        return False

    moves = [
        f(s - 2, step + 1),
        f(s // 2, step + 1)
    ]

    if step % 2 == 0:
        return any(moves)
    return all(moves)

for s in range(88, 20**5):
    if f(s):
        print(s)


# 180


