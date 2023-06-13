import numpy as np
R = np.array([
    [12, 10, 6, 9, 8, 23, 5, 2],
    [ 0, 1, 2, 3, 4, 5, 6, 7],
    [-10,-20,-80,-40,29,39,10,50],
    [-5,-9,-4,8,7,61,5,19],
    [42,0,69,4,6,46,66,6],
    [1,1,2,2,3,3,5,5],
    [0,2,4,6,8,10,12,14],
    [2,3,5,7,11,13,17,19]
    ])
print("Matriks bujursangkar R adalah:")
print(R)
diagonal = np.diag(R)
print("\nElemen-elemen diagonal utamanya adalah:",diagonal)
kali,jumlah = 1,0
for i in diagonal:
    kali *= i
    jumlah += i
def jum(lst):
    a = 0
    for i in lst:
        a+=i
    return a
print("Hasil perkalian elemen diagonal utamanya adalah:",kali)
print("Hasil penjumlahan elemen diagonal utamanya adalah=",jumlah)
print("\nElemen-elemen pada baris ketujuh adalah: ",R[6])
print("Hasil penjumlahan elemen baris ketujuh adalah =",jum(R[6]))
print("Elemen-elemen pada kolom keempat adalah: ",R[:,3])
print("Hasil penjumlahan elemen kolom keempat adalah =",jum(R[:,3]))
T = R.copy()
T[:,1],T[:,5]=T[:,5],T[:,1].copy()
print("\nMatriks T sebagai hasil dari matriks R yang telah ditukar elemen kolom kedua dengan kolom keenam adalah:")
print(T)
print("\nArray C yang berisi hasil penjumlahan elemen baris ketujuh dengan kolom keempat matriks R adalah:",
    R[6]+R[:,3])
