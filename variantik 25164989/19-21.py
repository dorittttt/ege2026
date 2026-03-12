# def f(s1, s2, step = 1):#p1 v2 p3 v4 p5
#     if s1 + s2 >= 207 and step == 3:
#         return True
#     if (s1 + s2 >= 207 and step < 3) or (s1 + s2 < 207 and step == 3):
#         return False
#     moves = [
#         f(s1 + 1, s2, step + 1),
#         f(s1, s2 + 1, step + 1),
#         f(s1, s2 * 2, step + 1),
#         f(s1 * 2, s2, step + 1),
#     ]
#     if step % 2 == 0:
#         return any(moves)
#     return any(moves)
#
# for i in range(1, 189 + 1):
#     if f(17, i):
#         print(i)
#
# def f(s1, s2, step=1):  # p1 v2 p3 v4 p5
#     if s1 + s2 >= 207 and step == 4:
#         return True
#     if (s1 + s2 >= 207 and step < 4) or (s1 + s2 < 207 and step == 4):
#         return False
#     moves = [
#         f(s1 + 1, s2, step + 1),
#         f(s1, s2 + 1, step + 1),
#         f(s1, s2 * 2, step + 1),
#         f(s1 * 2, s2, step + 1),
#     ]
#     if step % 2 != 0:
#         return any(moves)
#     return all(moves)
#
#
# for i in range(1, 189 + 1):
#     if f(17, i):
#         print(i)
def f(s1, s2, step=1):  # p1 v2 p3 v4 p5
    if s1 + s2 >= 207 and step == 3:
        return True
    if (s1 + s2 >= 207 and step < 3) or (s1 + s2 < 207 and step == 3):
        return False
    moves = [
        f(s1 + 1, s2, step + 1),
        f(s1, s2 + 1, step + 1),
        f(s1, s2 * 2, step + 1),
        f(s1 * 2, s2, step + 1),
    ]
    if step % 2 == 0:
        return any(moves)
    return all(moves)


for i in range(1, 189 + 1):
    if f(17, i):
        print(i)
# 85
# 93