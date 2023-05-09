def hitung_fpb(x, y, z):
    "Menghitung FPB dari tiga bilangan"
    def hitung_fpb_dua(x, y):
        "Menghitung FPB dari dua bilangan"
        while y != 0:
            x, y = y, x % y
        return x
    
    fpb_xy = hitung_fpb_dua(x, y)
    fpb_xyz = hitung_fpb_dua(fpb_xy, z)
    return fpb_xyz