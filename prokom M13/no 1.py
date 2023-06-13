U = [[7.8, 1.7, 4.8, 0.4], [3.0, 9.6, 9.5, 1.3], [1.3, 1.6, 2.1, 4.6]]
V = [[4.4, 8.2, 5.1], [8.1, 5.4, 0.5], [3.8, 5.1, 2.4], [1.4, 3.8, 9.1]]
D = [1, 4, 2, 3]
print("Matriks sembarang U berdimensi 3x4 adalah:")
for i in range(len(U)):
    for j in range(len(U[i])):
        print(U[i][j],end=' ')
    print()
print("\nElemen diagonal utama dari matriks diagonal D adalah:",end=' ')
for i in range(len(D)):
    print(D[i],end=' ')
print("\n\nMatriks sembarang V berdimensi 4x3 adalah:")
for i in range(len(V)):
    for j in range(len(V[i])):
        print(V[i][j],end=' ')
    print()
print("\nMatrik UD merupakan hasil perkalian U dan D:")
UD = [[0 for j in range(len(D))] for i in range(len(U))]
for i in range(len(U)):
    for j in range(len(D)):
        UD[i][j] = round(U[i][j]*D[j],1)
        print(UD[i][j],end=' ')
    print()
DV = [[0 for j in range(len(D))] for i in range(len(V))]
print("\nMatrik DV merupakan hasil perkalian D dan V:")
for i in range(len(D)):
    for j in range(len(V[i])):
        DV[i][j] = round(V[i][j]*D[i],1)
        print(DV[i][j],end=' ')
    print()
