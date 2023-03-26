#program persamaan kuadrat ax^2+bx+c
#dengan D=b^2-4ac
a, b, c = int(input()), int(input()), int(input())
D = b**2-4*a*c #D=deskriminan
X1 = (-b+(D)**1/2)/2*a
X2 = (-b-(D)**1/2)/2*a
#testing => a,b,c = 1,2,1 D=0
#testing => a,b,c = 1,3,5 D<0
#testing => a,b,c = 2,5,1 D>0

if D>0:
    print('ada dua akar berlainan, yaitu X1 dan X2')
    print("Nilai dari X1 =", X1,"dan X2 =", X2)
elif D==0:
    print('ada satu akar (akar kembar), X1 = X2')
    print("Nilai dari X1 =", X1,"dan X2 =", X2)
else:
    print('cukup ditulis "akar imajiner"')
    print("Nilai dari X1 =", X1,"dan X2 =", X2)
    