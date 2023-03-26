a = input("Masukan Nilai a")
b = input("Masukan Nilai b")
c = input("Masukan Nilai c")

a = int(a)
b = int(b)
c = int(c)

#Nilai Deskriminan
D = (b**2-4*a*c)**1/2

#Nilai X1 dan X2 dari persamaan ax^2+bx+c
X1 = (-b + D)/(2*a)
X2 = (-b - D)/(2*a)