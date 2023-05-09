def bulan_taun(bulan):
    list_bln=['January','February','March','April','Mei','June','July','August','September','October','November','December']
    return list_bln[bulan-1]

def jmlh_hari(tahun):
    list_jmlh_hari = [28,29]
    if tahun %4 ==0:
        return list_jmlh_hari[1]
    else:
        return list_jmlh_hari[0]
    