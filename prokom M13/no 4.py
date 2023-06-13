
import numpy as np
a = np.array([1, 4, 7])
print("Vektor a =",a)
mag_a = round((a[0]**2+a[1]**2+a[2]**2)**(1/2),1)
print("Magnitude vektor a =",mag_a)
b = np.array([5, 7, 2])
print("Vektor b =",b)
mag_b = round((b[0]**2+b[1]**2+b[2]**2)**(1/2),1)
print("Magnitude vektor b =",mag_b)
sudut = np.degrees(np.arccos(np.dot(a,b)/(mag_a*mag_b)))
print(sudut)
print("Hasil kali titik (dot product) vektor a dan b berupa skalar =",
    np.dot(a,b))
d = round(sudut//1)
m = ((sudut-d)*60)
s = round((m-m//1)*60,2)
print("Sudut yang terbentuk antara vektor a dan b dalam DMS adalah =",d,round(m//1),s)
c = np.cross(a,b)
print("Hasil kali silang (cross product) vektor a = b berupa vektor =",c)
L_seg = round(((c[0]**2+c[1]**2+c[2]**2)**(1/2))/2,5)
print("Luas segitiga yang tertentu oleh vektor a dan b =",L_seg)
