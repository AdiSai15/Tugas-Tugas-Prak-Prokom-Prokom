#No1




#atau Program ini????
mahasiswa_1 = {"Adi", "Eko", "Ami", "Ipung", "Arif", "Alam", "Nadine", "Allysa", "Rafillia", "Nabila"}
uts_diatas_80 = {"Adi", "Ami", "Alam", "Allysa", "Rafillia"}
uas_dibawah_80 = {"Adi","Allysa", "Rafillia","Arif", "Ipung"}

#nilai A (uts_diatas_80 & uas_diatas_80)
A = uts_diatas_80 & uas_dibawah_80
print('Yang mendapat nilai A adalah :', A)
print('Banyaknya orang yang mendapat nilai A :', len(A))
#nilai B(uts_diatas_80 atau uas_diatas_80)
B = uts_diatas_80 or uas_dibawah_80
print('Yang mendapat nilai B adalah :', B)
print('Banyaknya orang yang mendapat nilai B :', len(B))
#nilai C(tidak uts_diatas_80 dan tidak uas_diatas_80)
C = mahasiswa_1.difference(uts_diatas_80.union(uas_dibawah_80))
print('Yang mendapat nilai C adalah :', C)
print('Banyaknya orang yang mendapat nilai C :', len(C))
