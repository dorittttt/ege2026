for a in range(1 ,1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not (
                    (5 < y) or (x > 32) or ((x + 2 * y) < a)
            ):
                flag = False
    if flag:
        print(a)

