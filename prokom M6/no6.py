list_A = [1, 1, 2, 3, "Agus", 5, 8, 13, "Rafilia", 21, 34, 55, 89, "Tini"]
list_B = [1, 2, 3, "Tonga", 4, 5, 6, 7, 8, "Safai", 8, 9, 9, 9, 10, 10, 11, "Udin", "Agus", 12, 12, 13]

common_elements = list(set(list_A) & set(list_B))
print("Elemen-elemen yang ada pada kedua list:", common_elements)

semua_elemen = list(set(list_A + list_B))
print("Gabungan semua elemen dari kedua list:", semua_elemen)

elemen_unik_b = list(set(list_B) - set(list_A))
print("Elemen-elemen yang terdapat pada list_B namun tidak terdapat pada list_A:", elemen_unik_b)

elemen_unik_a = list(set(list_A) - set(list_B))
print("Elemen-elemen yang terdapat pada list_A namun tidak terdapat pada list_B:", elemen_unik_a)

symmetric_difference = list(set(list_A) ^ set(list_B))
print("Gabungan elemen yang hanya terdapat pada list_A dan yang hanya juga terdapat pada list_B:", symmetric_difference)
