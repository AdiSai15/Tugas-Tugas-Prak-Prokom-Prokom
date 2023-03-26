# a. Bilangan bulat positip dari 1 sampai 100 yang habis dibagi 3
set_a = set(range(3, 101, 3))
print("a. Himpunan bilangan bulat positip dari 1 sampai 100 yang habis dibagi 3:")
print(set_a)
print("Jumlah elemen: ", len(set_a))
print()

# b. Bilangan bulat positip dari 1 sampai 100 yang habis dibagi 5
set_b = set(range(5, 101, 5))
print("b. Himpunan bilangan bulat positip dari 1 sampai 100 yang habis dibagi 5:")
print(set_b)
print("Jumlah elemen: ", len(set_b))
print()

# c. Bilangan bulat positip dari 1 sampai 100 yang habis dibagi 3 dan 5
set_c = set_a.intersection(set_b)
print("c. Himpunan bilangan bulat positip dari 1 sampai 100 yang habis dibagi 3 dan 5:")
print(set_c)
print("Jumlah elemen: ", len(set_c))
print()

# d. Bilangan bulat positip dari 1 sampai 100 yang habis dibagi 3 atau 5
set_d = set_a.union(set_b)
print("d. Himpunan bilangan bulat positip dari 1 sampai 100 yang habis dibagi 3 atau 5:")
print(set_d)
print("Jumlah elemen: ", len(set_d))
print()

# e. Bilangan bulat positip dari 1 sampai 100 yang habis dibagi 3 tetapi tidak habis dibagi 5
set_e = set_a.difference(set_b)
print("e. Himpunan bilangan bulat positip dari 1 sampai 100 yang habis dibagi 3 tetapi tidak habis dibagi 5:")
print(set_e)
print("Jumlah elemen: ", len(set_e))
print()

# f. Bilangan bulat positip dari 1 sampai 100 yang habis dibagi 5 tetapi tidak habis dibagi 3
set_f = set_b.difference(set_a)
print("f. Himpunan bilangan bulat positip dari 1 sampai 100 yang habis dibagi 5 tetapi tidak habis dibagi 3:")
print(set_f)
print("Jumlah elemen: ", len(set_f))
print()

# g. Bilangan bulat positip dari 1 sampai 100 yang tidak habis dibagi 3 dan 5
set_g = set(range(1, 101)).difference(set_a.union(set_b))
print("g. Himpunan bilangan bulat positip dari 1 sampai 100 yang tidak habis dibagi 3 dan 5:")
print(set_g)
print("Jumlah elemen: ", len(set_g))
print()

# h. Bilangan bulat positip dari 1 sampai 100 yang tidak habis dibagi 3 atau 5
set_h = set(range(1, 101)).difference(set_a.intersection(set_b))
print("h. Himpunan bilangan bulat positip dari 1 sampai 100 yang tidak habis dibagi 3 atau 5:")
print(set_h)
print("Jumlah elemen: ", len(set_h))
print()

# i. Bilangan bulat positip dari 1 sampai 100 yang habis dibagi 3 ataupun yang habis dibagi 5, tetapi tidak habis dibagi keduanya
