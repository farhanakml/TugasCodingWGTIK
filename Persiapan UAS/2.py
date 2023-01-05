# a = tuple([int(i)for i in input().split()])

a = tuple(input().split())

positif = 0
negatif = 0

# for i in a:
#     if i > 0:
#         positif += 1
#     if i < 0:
#         negatif += 1

for i in a:
    if int(i) > 0:
        positif += 1
    if int(i) < 0:
        negatif += 1

print("Positif : {}\nNegatif : {}".format(positif,negatif))