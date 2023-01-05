# a = input().split()
a = [int(i) for i in input().split()]
b = len(a)
jumlah = 0

# for i in a:
#     jumlah += int(i)

for i in a:
    jumlah += int(i)

c = jumlah/b

print("{:.3f}".format(c))