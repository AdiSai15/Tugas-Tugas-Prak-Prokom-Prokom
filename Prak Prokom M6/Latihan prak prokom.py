#latihan no 1
#buatlah outputnya agar terbalik dengan teknik slicing
azimuth = [0, 45, 90, 135, 180, 225, 270, 360]
print(azimuth[::-1])


#latihan no 2
#gunakan list azimuth no 1 untuk perhitungan sin, cos, tan, dll
azimuth = [0, 45, 90, 135, 180, 225, 270, 360]
import math
azimuth = ['Sin', 'Cos', 'Tan', 'Cotan', 'Cosec', 'Sec']
print("\t\t","0","\t ","45","\t ","90","\t ","135","\t ","180","\t ","225","\t","270","\t ","360")
print("------------------------------------------------------------------------------")
i = 0
import math
from math import*
while(i<6):
    if i == 0:
        print(azimuth[i],"\t",int(math.sin(radians(0))),
            "\t","{:.3f}".format(math.sin(radians(45))),"\t "," ", 
            (int(math.sin(radians(90)))),"\t ","{:.3f}".format(math.sin(radians(135)))," ", 
            int(math.sin(radians(180))),"\t " ,"{:.3f}".format(math.sin(radians(225))),"\t", 
            int(math.sin(radians(270))),"\t ",
            int(abs(math.sin(radians(360)))))
    if i == 1:
        print(azimuth[i],"\t",int(math.cos(radians(0))),
            "\t","{:.3f}".format(math.cos(radians(45))),"\t "," ", 
            (int(math.cos(radians(90)))),"\t","{:.3f}".format(math.cos(radians(135)))," ", 
            int(math.cos(radians(180))),"\t " ,"{:.3f}".format(math.cos(radians(225))),"\t ", 
            int(math.cos(radians(270))),"\t ",
            int(abs(math.cos(radians(360)))))
    if i == 2:
        print(azimuth[i],"\t",int(math.tan(radians(0))),"\t ", 
            int(math.tan(radians(45))),"\t "," ", "-","\t ",
            int(math.tan(radians(135))),"\t ", 
            int(math.tan(radians(180))),"\t\t" ,
            int(math.tan(radians(225))),"\t\t ", "-","\t ",
            int(abs(math.tan(radians(360)))))
    if i == 3:
        print(azimuth[i],"\t","-","\t ",
            int(1/math.tan(radians(45))),"\t ",
            int(1/math.tan(radians(90))),"\t ",
            int(1/math.tan(radians(135))),"\t ","-","\t\t",
            int(1/math.tan(radians(225))),"\t\t ",
            int(1/math.tan(radians(270))),"\t ","-")
    if i == 4:
        print(azimuth[i],"\t","-","\t","{:.3f}".format(1/math.sin(radians(45))),"\t ",
            int(1/math.sin(radians(90))),
            "\t ","{:.3f}".format(1/math.sin(radians(135))),
            " ",
            "-","\t " ,"{:.3f}".format(1/math.sin(radians(225))),"\t",
            int(1/math.sin(radians(270))),"\t ","-")
    if i ==5:
        print(azimuth[i],"\t",
            int((1/math.cos(radians(0)))),"\t",
            "{:.3f}".format(1/math.cos(radians(45))),"\t ",
            "-" "\t",
            "{:.3f}".format(1/math.cos(radians(135)))," ",
            int(1/math.cos(radians(180)))," " ,
            "{:.3f}".format(1/math.cos(radians(225))),"\t ","-","\t ",
            int(1/math.cos(radians(360))))
    i+=1
print("\nNote: ""\n- = tidak terdefinisi")
print("\nProgram selesai")


#latihan no 3
nama = [('paijo', 12345, 123.45), ('indah', 13412, 234.56), ('joko', 90289, 345.67), ('gilang', 32948, 456.78), ('lala', 45829, 567.89)]
for x in nama:
    for y in x:
        print(y, end='\n')
    print(' ')
#atau 
for x in nama:
    for y in x:
        print(y)
    print(' ')


#latihan no 4
tupel = (22, [12,32,91,143,948,12,844,1,3], 99, 111, 22, 121, 22, 180, 22)
#a hitung berapa banyak angka 22 pada tuple
hitung = 0 
for x in tupel:
    if x == 22:
        hitung +=1
print('Banyaknya angka 22 dalam tupel adalah', hitung)

#b lakukan operasi untuk mengecek apakah isi dari tupel tersebut bernilai sama atau tidak
tupel = (22, [12,32,91,143,948,12,844,1,3], 99, 111, 22, 121, 22, 180, 22)

if all(eliminasi == tupel[0] for eliminasi in tupel):
    print("Semua elemen tuple bernilai sama")
else:
    print("Terdapat elemen pada tuple yang memiliki nilai berbeda")

#c copy nilai 111,22,121 ke dalam tupel baru
tupel = (22, [12,32,91,143,948,12,844,1,3], 99, 111, 22, 121, 22, 180, 22)
new_tupel = tupel[3:6]
print('Tupel baru adalah', new_tupel)


#latihan no 5
x = [12,32,91,143,948,12,844,1,3]
x[::2]=[9,8,7,6,5,4][:len(x[::2])] #mengganti nilai dengan rentang 2 dengan menggunakan nomor indeks
print(x)