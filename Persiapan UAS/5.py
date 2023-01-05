n = int(input())

teks = "@informatika.com"

for i in range(n):
    a,b,c = input().split()

    print((a+b+c+teks).lower())
