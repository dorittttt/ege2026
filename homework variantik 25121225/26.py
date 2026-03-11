# f = open(r"26_24570.txt")
# n = f.readline()
# data = [[int(i) for i in row.split()] for row in f]
# # for id, mark1, mark2, mark3, mark4, mark5, price in data:
#
# # data = sorted(data, key=lambda x:(
# #     -(sum(x[1:6]) / 5), x[-1], x[0]
# # ))
# # for i in data[:5]:
# #     print(i)
# data2 = []
#
# for id, mark1, mark2, mark3, mark4, mark5, price in data:
#     data2.append([id, ((mark1 + mark2 + mark3 + mark4 + mark5 ) / 5), price])
# data2 = sorted(data2, key=lambda x:(
#     -x[1], x[-1], x[0]
# ))
# top = []
# med = []
# for id, avg, price in data2:
#     if avg > 80 and price <= 5000:
#         top.append([id, avg, price])
#     if avg <= 80 and price <= 5000:
#         med.append([id, avg, price])
# # print(top)
# # print(med[:5])
# budget = 0
# for id, avg, price in top:
#     budget += price
# print(budget)
f = open(r"26_24570.txt")
n = f.readline()
data = [[int(i) for i in row.split()] for row in f]
# for id, mark1, mark2, mark3, mark4, mark5, price in data:

# data = sorted(data, key=lambda x:(
#     -(sum(x[1:6]) / 5), x[-1], x[0]
# ))
# for i in data[:5]:
#     print(i)
data2 = []

for id, mark1, mark2, mark3, mark4, mark5, price in data:
    data2.append([id, ((mark1 + mark2 + mark3 + mark4 + mark5 ) / 5), price])
data2 = sorted(data2, key=lambda x:(
    -x[1], x[-1], x[0]
))
top = []
med = []
for id, avg, price in data2:
    if avg > 80 and price <= 5000:
        top.append([id, avg, price])
    if avg <= 80 and price <= 5000:
        med.append([id, avg, price])
# print(top)
# print(med[:5])
budget = 0
for id, avg, price in top:
    budget += price
print(budget)
