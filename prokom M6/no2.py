#for
k_angka = [5, 2, 1, 2.5, 5, 9, 2, 1.5, 9, 6, 6, 3, 7, 8, 2]
total = 0
hitung = 0
for num in k_angka:
    total += num
    hitung += 1
nilai_rata_rata = total / hitung
print("Nilai rata-rata dari list adalah:", nilai_rata_rata)

#while
k_angka = [5, 2, 1, 2.5, 5, 9, 2, 1.5, 9, 6, 6, 3, 7, 8, 2]
total = 0
hitung = 0
i = 0

while i < len(k_angka):
    total += k_angka[i]
    hitung += 1
    i += 1

nilai_rata_rata = total / hitung
print("Nilai rata-rata dari list adalah:", nilai_rata_rata)