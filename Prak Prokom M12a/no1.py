import numpy as np
mtrx_A = np.arange(18).reshape(3,3,2)
print(mtrx_A)
print("Nilai Maks:",np.max(mtrx_A)) #nilai maks
print("Nilai Min:",np.min(mtrx_A)) #nilai min
print("Rerata:",np.mean(mtrx_A)) #nilai rata-rata
print("Std Dev:",np.std(mtrx_A)) #standar deviasi
print("Varians:",np.var(mtrx_A)) #varians
#det_mtrx_A = np.linalg.det(mtrx_A)
mtrx_A1=np.array([
                [[0,1],
                [2,3],
                [3,5]],

                [[5,6],
                [8,9],
                [10,11]],
                
                [[12,13],
                [14,16],
                [16,17]]
                ])
#print("Determinan:",int(det_mtrx_A)) #eror karena dimensi
#print("Determinan:",np.linalg.det(mtrx_A1)) #eror karena dimensi

#CARA LAIN MUNGKIN ??
matriks = [[[0,1,2], [3, 4, 5], [6, 7, 8]],
            [[9, 10, 11], [12, 13, 14], [15, 16, 17]]]

matrik_A = np.array(matriks)
print(matrik_A)
print("Nilai Maks:",np.max(matrik_A)) #nilai maks
print("Nilai Min:",np.min(matrik_A)) #nilai min
print("Rerata:",np.mean(matrik_A)) #nilai rata-rata
print("Std Dev:",np.std(matrik_A)) #standar deviasi
print("Varians:",np.var(matrik_A)) #varians
print("Determinan",np.linalg.det(matrik_A)) #determinan