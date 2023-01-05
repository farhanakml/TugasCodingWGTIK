import numpy as py
baris_bilangan = input().split()
set_bilangan = set(baris_bilangan)

jumlah = 0
n_data = 0

for bilangan in baris_bilangan:
    jumlah += int(bilangan)
    n_data += 1

rata = jumlah / n_data
print("{:.1f}".format(round(rata)))
