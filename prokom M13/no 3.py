import numpy as np
m_kolom = np.array([[5.5, 9.1, 1.8, 5.1, 6.9]]).transpose()
m_baris = np.array([[6.4, 5.2, 1.2, 9.4, 0.6]])
print("Matriks kolom adalah:")
for i in m_kolom: 
    print(i[0])
print("\nMatriks baris adalah:")
for i in m_baris[0]:
    print(i,end=' ')
print("\n\nMatriks hasil perkalian kolom baris nya adalah:")
print(np.dot(m_kolom,m_baris))
print("\nMatriks hasil perkalian baris kolom nya adalah:")
print(np.dot(m_baris,m_kolom))
