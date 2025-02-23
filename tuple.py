# tup = (1, 2, 3)
# for i in tup:
# print(i)
# (x, y) = (99, 98)
# print(x)
d = dict()
d["cards"] = 2
d["apple"] = 4
for k, v in d.items():
    print(k, v)
    # this is how we creat list of two tuples

    # tuples are comparable
# if ("jones", "sally") < ("jones", "sam"):
# print("true")
sorted(d.items())
print(d)
# sorting by value
c = {"a": 10, "b": 20, "c": 30}
tmp = list()
for k, v in c.items():
    tmp.append((v, k))
print(tmp)

tmp = sorted(tmp)
print(tmp)
