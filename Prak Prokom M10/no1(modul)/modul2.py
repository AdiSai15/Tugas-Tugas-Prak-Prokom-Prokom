from scipy.optimize import minimize_scalar
from modul1 import*
from modul1 import volume_kotak

def fungsi_objektif(x):
    return -volume_kotak(12-2*x)

hasil = minimize_scalar(fungsi_objektif, bounds=(0, 6), method='bounded')
ukuran_pemotongan = hasil.x
volume_terbesar = -hasil.fun

print("Ukuran pemotongan yang menghasilkan kotak kardus dengan volume terbesar adalah", ukuran_pemotongan, "m")
print("Volume kotak terbesar yang dapat dihasilkan adalah", volume_terbesar, "m^3")
