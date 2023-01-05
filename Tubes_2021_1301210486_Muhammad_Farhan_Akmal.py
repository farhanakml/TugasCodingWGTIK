def read():
    f = open('data.txt','r')
    return f

data_buku = {}
stok_buku = []

def data():
    f = read()
    for buku in f:
        ISBN, stok, senin, selasa, rabu, kamis, jumat, sabtu = buku.split()
        data_buku.update({ISBN : sum(list(map(int,[senin, selasa, rabu, kamis, jumat, sabtu])))})
        stok_buku.append(int(stok))
    f.close()

def favorit():
    a = max(data_buku, key=data_buku.get)
    return print(a,"adalah ISBN buku terfavorit !")

def laporan_stok():
    i = 0
    for k, v in data_buku.items():
        if v == stok_buku[i]:
            print(k,"adalah ISBN buku yang harus di restock !")
        i += 1

def main():
    data()
    print(data_buku)
    favorit()
    laporan_stok()

main()
