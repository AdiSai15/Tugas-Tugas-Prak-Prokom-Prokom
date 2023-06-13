import numpy as np
U = np.array([[7.8, 1.7, 4.8, 0.4], [3.0, 9.6, 9.5, 1.3], [1.3, 1.6, 2.1, 4.6]])
V = np.array([[4.4, 8.2, 5.1], [8.1, 5.4, 0.5], [3.8, 5.1, 2.4], [1.4, 3.8, 9.1]])
D = np.array([1, 4, 2, 3])
print("Matriks sembaranh U berdimensi 3x4 adalah:")
print(U)
print("\nElemen diagonal utama dari matriks diagonal D adalah:")
D = np.diag(D)
print(D)
print("\nMatriks sembarang V berdimensi 4x3 adalah:")
print(V)
print("\nMatrik UD merupakan hasil perkalian U dan D:")
print(np.dot(U,D))
print("\nMatrik DV merupakan hasil perkalian D dan V:")
print(np.dot(D,V))