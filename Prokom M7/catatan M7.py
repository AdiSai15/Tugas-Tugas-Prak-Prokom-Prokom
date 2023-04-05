C = set(range(1002,1101,3))
print('List C:', C)
print(len(C))
B = list(range(1002,1101,3))
print('List B:', B)

#A={"Linda",39,"Rajid",41,"Diba",37}

#JADIKAN SET
A=set(["Linda",39,"Rajid",41,"Diba",37])
#jadikan list A tersebut dengan membuang 41,"Diba"
A.remove(41)
A.remove("Diba")
print(A)

#DIFFERENCE UPDATE
A={"Linda",39,"Rajid",41,"Diba",37}
Buang={"Diba", 41}
A.difference_update(Buang)
print(A)

#Looping
A={"Linda",39,"Rajid",41,"Diba",37}
Buang={"Diba", 41}
for nilai in Buang:
  A.remove(nilai)
print(A)

#Membuat Dictionary
#menggunakan {} dan langsung memberikan kunci(key) dan nilai (value)
kamus = {'123456' : 'Rochmad M', 'Lahir' : 'Solo', 12345 : 'No.Mhs', 'Umur' : 57, "AD" : 'Solo'}
print(kamus)
#menggunakan dict (key=value) dipisahkan dengan =
#syarat kunci tidak boleh number, harus pakai string, tidak boleh menggunakan petik
kamus = dict(123456 = 'Rochmad M', Lahir = 'Solo', 12345 = 'No.Mhs', Umur = 57, AD = 'Solo')
print(kamus)