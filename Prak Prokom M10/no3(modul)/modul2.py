import math
from scipy.optimize import minimize
from modul1 import vol_silinder, luas_silinder_tanpa_tutup

def fungsi_objektif(x):
    r, t = x
    return luas_silinder_tanpa_tutup(r, t)

def batasan1(x):
    return x[0]-0.001

def batasan2(x):
    return x[1]-0.001

def batasan3(x):
    return 8000*math.pi - vol_silinder(x[1],x[0])

batas_bawah = [0.001, 0.001]
batas_atas = [8000*math.pi/(4*(batas_bawah[0]**2)), 8000*math.pi/(4*(batas_bawah[1]**2))]
batasan = [(batas_bawah[0], batas_atas[0]), (batas_bawah[1], batas_atas[1])]
batasan_kons = [{'type': 'ineq', 'fun': batasan1},
                {'type': 'ineq', 'fun': batasan2},
                {'type': 'ineq', 'fun': batasan3}]

hasil = minimize(fungsi_objektif, [batas_bawah[0], batas_bawah[1]], method='SLSQP', bounds=batasan, constraints=batasan_kons)
t = hasil.x[0]
r = hasil.x[1]

print("Tinggi silinder yang digunakan adalah", t, "cm")
print("Jari-jari alas silinder yang digunakan adalah", r, "cm")
print("Volume aluminium yang digunakan adalah", vol_silinder(r, t), "cm^3")
