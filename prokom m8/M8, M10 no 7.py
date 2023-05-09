#a (tanpa argumen)
def akar_kuadrat():
    print('Program menghitung akar persamaan kuadrat ax2 + bx + c = 0')
    global deskriminan  # variabel deskriminan sebagai variabel global
    for i in range (0,3):
        if i ==0:
            print("Hitungan pertama")
        elif i ==1:
            print("\nHitungan kedua")
        else:
            print("\nHitungan ketiga")
        a = float(input("Masukkan nilai koefisien a = "))
        b = float(input("Masukkan nilai koefisien b = "))
        c = float(input("Masukkan nilai koefisien c = "))
        deskriminan = ((b**2)-(4*a*c))
        x1 = (-b+(deskriminan**(1/2)))/(2*a)
        x2 = (-b-(deskriminan**(1/2)))/(2*a)
        if deskriminan > 0:
            print('Nilai deskriminan positif, maka akar-akarnya adalah:'
                  '\nx1=', x1,
                  '\nx2=', x2)
        elif deskriminan == 0:
            print('Nilai deskriminan = 0, maka akarnya kembar x1 = x2, yaitu:'
                  '\nx1=', x1,
                  '\nx2=', x2)
        elif deskriminan < 0:
            print('Nilai deskriminan negatif, akarnya imajiner')

akar_kuadrat()

#b (Dengan argumen)
def akar_kuadrat(x1,x2):
    print('Program menghitung akar persamaan kuadrat ax2 + bx + c = 0')
    global deskriminan  # variabel deskriminan sebagai variabel global
    for i in range (0,3):
        if i ==0:
            print("Hitungan pertama")
        elif i ==1:
            print("\nHitungan kedua")
        else:
            print("\nHitungan ketiga")
        a = float(input("Masukkan nilai koefisien a = "))
        b = float(input("Masukkan nilai koefisien b = "))
        c = float(input("Masukkan nilai koefisien c = "))
        deskriminan = ((b**2)-(4*a*c))
        x1 = (-b+(deskriminan**(1/2)))/(2*a)
        x2 = (-b-(deskriminan**(1/2)))/(2*a)
        if deskriminan > 0:
            print('Nilai deskriminan positif, maka akar-akarnya adalah:'
                  '\nx1=', x1,
                  '\nx2=', x2)
        elif deskriminan == 0:
            print('Nilai deskriminan = 0, maka akarnya kembar x1 = x2, yaitu:'
                  '\nx1=', x1,
                  '\nx2=', x2)
        elif deskriminan < 0:
            print('Nilai deskriminan negatif, akarnya imajiner')
    return(x1,x2)

akar_kuadrat('x1','x2')
