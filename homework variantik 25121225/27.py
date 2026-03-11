# f = open(r"27A_24566.txt")
# data = [[float(i) for i in row.split()] for row in f]
#
# claster1 = []
# claster2 = []
#
# for x, y in data:
#     if -5.5 <= x <= -1.5 and 2.5 <= y <= 6.5:
#         claster1.append([x, y])
#     if 27 <= x <= 32 and 10 <= y <= 17:
#         claster2.append([x, y])
#
# from math import *
# def find_center(claster):
#     center = None
#     rast = 10**10
#     for start in claster:
#         temp_rast = 0
#         for stop in claster:
#             temp_rast += dist(start, stop)
#         if temp_rast < rast:
#             rast = temp_rast
#             center = start
#     return center
#
# def find_anti_center(claster):
#     center = None
#     rast = 0
#     for start in claster:
#         temp_rast = 0
#         for stop in claster:
#             temp_rast += dist(start, stop)
#         if temp_rast > rast:
#             rast = temp_rast
#             center = start
#     return center
# x1, y1 = (find_center(claster1))
# x2, y2 = (find_center(claster2))
# x1_1, y2_1 = (find_anti_center(claster1))
# x2_2, y2_2 = (find_anti_center(claster2))
# print((x1 + x2 + x1_1 + x2_2) * 1000)
# print((y1 + y2 + y2_1 + y2_2) * 1000)

f = open(r"27B_24566.txt")
data = [[float(i) for i in row.split()] for row in f]

claster1 = []
claster2 = []
claster3 = []
claster4 = []
claster5 = []

for x, y in data:
    if -5.5 <= x <= -1.5 and 6 <= y <= 11:
        claster1.append([x, y])
    if 0 <= x <= 4 and -4 <= y <= 1:
        claster2.append([x, y])
    if 11 <= x <= 17 and -3 <= y <= 3:
        claster3.append([x, y])
    if 25 <= x <= 32 and 2 <= y <= 8:
        claster4.append([x, y])
    if 20 <= x <= 27 and 20 <= y <= 27:
        claster5.append([x, y])

from math import *
def find_center(claster):
    center = None
    rast = 10**10
    for start in claster:
        temp_rast = 0
        for stop in claster:
            temp_rast += dist(start, stop)
        if temp_rast < rast:
            rast = temp_rast
            center = start
    return center

def find_anti_center(claster):
    center = None
    rast = 0
    for start in claster:
        temp_rast = 0
        for stop in claster:
            temp_rast += dist(start, stop)
        if temp_rast > rast:
            rast = temp_rast
            center = start
    return center
x1, y1 = (find_center(claster1))
x2, y2 = (find_center(claster2))
x3, y3 = (find_center(claster3))
x4, y4 = (find_center(claster4))
x5, y5 = (find_center(claster5))
x1_1, y2_1 = (find_anti_center(claster1))
x2_2, y2_2 = (find_anti_center(claster2))
x3_3, y3_3 = (find_anti_center(claster3))
x4_4, y4_4 = (find_anti_center(claster4))
x5_5, y5_5 = (find_anti_center(claster5))
print((x1 + x2 + x1_1 + x2_2) * 1000)
print((y1 + y2 + y2_1 + y2_2) * 1000)
from itertools import combinations
max_mod_d = 0
coords = combinations()