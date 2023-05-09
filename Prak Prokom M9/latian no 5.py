def hitung_standar_deviasi(data):
    rata_rata = sum(data)/len(data)
    selisih_kuadrat = 0
    for nilai in data:
        selisih_kuadrat += (nilai-rata_rata)**2
    variansi = selisih_kuadrat/len(data)
    standar_deviasi = variansi ** 0.5
    return standar_deviasi

data = [3, 4, 5, 4, 9, 9]
sd = hitung_standar_deviasi(data)
print("Standar deviasi:", sd)

