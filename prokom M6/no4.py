#looping_list
list_A = [10, 20, 30, 40, "A", "B", "C", "D"]
tuple_A = (10, 20, 30, 40, "A", "B", "C", "D")
#for
for i in tuple_A:
    print(i, end=' ')
print()

#for & range
for i in range(len(tuple_A)):
    print(tuple_A[i], end=' ')
print()

#for range menampilkan no indeks
for i in range(len(tuple_A)):
    print("Indeks[" + str(i) + "] adalah:", tuple_A[i])

#while
i = 0
while i < len(tuple_A):
    print(tuple_A[i], end=' ')
    i += 1
print()

#list comprehension
[print(x, end=' ') for x in tuple_A]
print()


#script Control list (Masih Bingung)
tuple_A = (10, 20, 30, 40, "A", "B", "C", "D")
list_A = list(tuple_A)
d = tuple_A[:-2]
print(d)

for i in d:
    if isinstance(i, int): #isintance hanya digunakan untuk pengecekan integer
        if i >= 30 and i <= 50:
            print('Nilai ', str(i), 'adalah Angka Besar')
            print('Lihat apa kita mendapat sebuah teks')
        elif i >= 40:
            print('Nilai ', str(i), 'adalah Angka Lebih Besar')
        else:
            print('Nilai ', str(i), 'adalah Angka Kecil')
        print('if is finished')
tuple_A = tuple(d)
print('Finished')
