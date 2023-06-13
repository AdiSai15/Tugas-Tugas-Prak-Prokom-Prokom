import numpy as np 

z = 0.7632

matrix = np.random.uniform(low=-1, high=1, size=(5, 5))
nilai_terdekat = np.abs(matrix - z).min()

# Cetak matriks dan nilai terdekat
print("Matriks:")
print(matrix)
print("\nNilai terdekat dengan z =", z, "adalah:", nilai_terdekat)
