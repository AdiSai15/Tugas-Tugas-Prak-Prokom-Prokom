#mengganti nilai dalam indeks
A = ["Pota", 200,"B", 45, 1, 200]
A[3:5] = ["butet", 'padang']
a = A
print(A)
print(a)


# list
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemen = str(input(''))
if elemen in list_a:
    indeks = list_a.index(elemen)
    print(f'Elemen {elemen} terdapat pada indeks ke-{indeks} dalam list_a')
else:
    print(f'Elemen {elemen} tidak terdapat dalam list_a')

# tuple
tuple_a = ('a', 'b', 'c', 'd', 'e')
elemen = 'c'
if elemen in tuple_a:
    indeks = tuple_a.index(elemen)
    print(f'Elemen {elemen} terdapat pada indeks ke-{indeks} dalam tuple_a')
else:
    print(f'Elemen {elemen} tidak terdapat dalam tuple_a')

# set
set_a = {1, 2, 3, 4, 5, 6}
elemen = 3
if elemen in set_a:
    indeks = list(set_a).index(elemen)
    print(f'Elemen {elemen} terdapat pada indeks ke-{indeks} dalam set_a')
else:
    print(f'Elemen {elemen} tidak terdapat dalam set_a')
