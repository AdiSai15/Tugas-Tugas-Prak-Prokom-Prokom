def hitung_kpk(x, y, z):
    """Menghitung KPK dari tiga bilangan"""
    def hitung_fpb_dua(x, y):
        """Menghitung FPB dari dua bilangan"""
        while y != 0:
            x, y = y, x % y
        return x
    
    kpk_xy = (x*y) // hitung_fpb_dua(x, y)
    kpk_xyz = (kpk_xy * z) // hitung_fpb_dua(kpk_xy, z)
    return kpk_xyz
