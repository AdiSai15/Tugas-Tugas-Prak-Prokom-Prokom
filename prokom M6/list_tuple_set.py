#tuple tidak bisa diganti nilainya, tapi bisa ditambah, memiliki indeks dan bisa diurutkan, boleh memiliki nilai yang sama
#set bisa diganti nilainya, tapi bisa di tambah dan bisa dihapus tidak memiliki indeks(tidak bisa diurutkan), nilainya unik
#list memiliki indeks yang sama, bebas, bisa diganti
A = ["Pota", 200,"B", 45, 1, 200]
#fungsi len untuk menghitung banyaknya elemen data
B = tuple(A)
C = set(A)
print(B,C)
#akses list A
print(A[2:-1])
print(A[2])
print(A[:2])
print(A[2:])
#tanpa tanda kurung
#cara pertama
for i in A: 
    print(i,end=' ')
print()
#cara kedua
for i in range(len(A)):
    print(A[i], end=' ')
print()

#cara kegita
x=0
while x<len(A):
    print(A[x], end=' ')
    x+=1
print()

#mengganti nilai dalam indeks
A = ["Pota", 200,"B", 45, 1, 200]
A[3:5] = ["butet", 'padang']
a = A
print(A)
print(a)

#del[menghapus indeksnya]
#clear[menghapus semua data]
#remove [ ]
#pop[]
A = ["Pota", 200,"B", 45, 1, 200]
A[3:5] = ["butet", 'padang']
a = A
print(A)
print(a)
print(A)
#menambahkan nilai menggunakan [append] dan [insert]
#insert digunakan untuk menyisipkan item pada indeks tertentu
#append digunakan untuk mengambahkan item data pada bagian akhir
A = ["Pota", 200,"B", 45, 1, 200]
A[3:5] = ["butet", 'padang']
a = A
print(A)
print(a)
A.append('Modul')
print(A)
#cara menambahkan lebih dari satu nilai
A = ["Pota", 200,"B", 45, 1, 200]
A[3:5] = ["butet", 'padang']
a = A
print(A)
print(a)
A.remove("Pota")
A+=['open', 'omdo']
print(A)
print(a)
A = A + ['open', 'omdo']


#menampilkan A unik
print(list(set(A)))
#menampilkan A menjadi unik
#set, list, tuple. menjadi construcktor jika ada ()
a=tuple()
type(a)
b= set()
type(b)
c=list()
type(c)
d = dict()
type(d)

#membuat list kosong cara kedua
A=[] #outputnya jika dimasukan typr(A) merupakan list
B=() #outputnya jika dimasukan type(B) merupakan tuple
C={} #outputnya jika dimasukan type(C) merupakan dictionary

#buatlah list kosong, masukan elemen pertama ke list kosong, jika ada yang sama tidak boleh ada yang sama
#program membuat list yang unik
A = ["Pota", 200,"B", 45, 1, 200]
B = []
for i in A:
    if i not in B:
        B.append(i)
print(B)


#TUPLE
Q = ("Pota", 200,"B", 45, 1, 200)
#buatlah codingan agar tuple q menjadi q = ("Pota", 20,"B", 45, 1, 20)
x=list(Q)
x[1] = 20
Q = tuple(x)
print(Q)


#cara kedua
print(Q[0])
print(Q[:1]) #ini yang dipakai jika menggunakan tuple
Q = Q[:1] + tuple([10]) + Q[2:]
print(Q)

#menambahkan
Q = ("Pota", 200,"B", 45, 1, 200)
Q = Q + ("Oke",)
print(Q)