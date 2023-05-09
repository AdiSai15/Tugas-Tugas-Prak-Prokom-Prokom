import random
def tebak():
    while True:
        tebakan = int(input("Tebak angka dari 1 sampai 500 : "))
        if 1<=tebakan<=500:
            break
        else:
            print("Harus dari 1 sampai 500")
    if random.randint(1,500) == tebakan:
        print("Benar")
    else:
        print("Coba lagi")
tebak()
