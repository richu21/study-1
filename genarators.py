def count(n) :
    yield n
    i = 1
    yield n + i
    i += 1
    print("hiii")
    yield n + i
    i += 1
    yield n + i

for x in count(10) :
    print(x)

# t = count(10)
# print(next(t))
# print(next(t))
# print(t.__next__)