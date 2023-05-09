def volume():
    #volume terbesar
    x = 0.01
    p = 12
    vol_awal = 0
    vol_baru = 0
    x_maks = 0

    #perulangan untuk menentukan volume terbesar
    while x<6:
        p = p-2*x
        l = p
        t = x
        vol_baru = p*l*t
        if vol_baru > vol_awal:
            vol_awal = vol_baru
            x_maks = x
        print(x)
        print(vol_baru)
        x+=0.01
    #pemanggilan akhir
    print("hasil iterasi memperoleh volume maksimum ")
    print("Volume =",vol_baru)
    print("nilai x maksimum =",x_maks)
    return vol_baru, x_maks


def volume_kotak(sisi):
    volume = sisi**3 - 8*(sisi**2) + 12*sisi
    return volume
