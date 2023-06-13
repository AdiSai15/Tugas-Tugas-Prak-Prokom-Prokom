import numpy as np 
mtrx_B =np.array([
                [5,1],
                [6,2],
                [7,1],
                [8,5],
                [9,10],
                [5,20],
                [9,25],
                [12,15],
                [9,4],
                [3,18],
                ]) #10x2
print(mtrx_B)

def konversi(kartesi):
    x = kartesi [:,0]
    y = kartesi [:,1]
    r = np.sqrt(x**2+y**2)
    alfa = np.arctan2(y, x)
    return np.column_stack((r,alfa))

mtrx_b_polar = konversi(mtrx_B)
print("Setelah dikonversi ke polar menjadi\n", mtrx_b_polar)
