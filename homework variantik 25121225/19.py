# def f(s, step = 1): #p1 v2 p3 v4 p5
#     if s <= 40 and step == 3:
#         return True
#     if (s <= 40 and step < 3) or (s > 40 and step == 3):
#         return False
#     moves = [
#         f(s  - 2, step + 1),
#         f(s  - 3, step + 1),
#         f(s  // 2, step + 1),
#     ]
#     if step % 2 == 0:
#         return any(moves)
#     return all(moves)
# for i in range(41, 1000):
#     if f(i):
#         print(i)
# def f(s, step = 1): #p1 v2 p3 v4 p5
#     if s <= 40 and step == 4:
#         return True
#     if (s <= 40 and step < 4) or (s > 40 and step == 4):
#         return False
#     moves = [
#         f(s  - 2, step + 1),
#         f(s  - 3, step + 1),
#         f(s  // 2, step + 1),
#     ]
#     if step % 2 != 0:
#         return any(moves)
#     return all(moves)
# for i in range(41, 1000):
#     if f(i):
#         print(i)

def f(s, step = 1): #p1 v2 p3 v4 p5
    if s <= 40 and step == 3:
        return True
    if (s <= 40 and step < 3) or (s > 40 and step == 3):
        return False
    moves = [
        f(s  - 2, step + 1),
        f(s  - 3, step + 1),
        f(s  // 2, step + 1),
    ]
    if step % 2 == 0:
        return any(moves)
    return all(moves)
for i in range(41, 1000000):
    if f(i):
        print(i)

# 87
# 88
# 168
# 169