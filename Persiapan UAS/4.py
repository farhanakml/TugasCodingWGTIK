a = set([int(i) for i in input().split()])
b = set([int(i) for i in input().split()])

c = a
for i in b:
    if i not in a:
        c.add(i)

d = set()
for i in b:
    if i in c:
        d.add(i)

print("a gabung b = {}\nb iris c = {}".format(c,d))