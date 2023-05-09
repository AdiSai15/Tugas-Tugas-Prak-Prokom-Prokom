# Menentukan tahun kabisat
# Sebelum tahun 1582 menggunakan Kalender Julian
def isLeapYear(year):
    if year > 1582:
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    return year % 4 == 0

# Menentukan jumlah hari dalam satu bulan
def daysInMonth(year, month):
    if(year == 1582 and month == 10):
        return 21 # Tanggal 5 s.d. 14 Oktober 1582 dihapus dari kalender
    elif month == 2: # Februari
        return 28 + isLeapYear(year) # 28 tahun biasa, tambah sehari untuk kabisat
    # Untuk selain Februari, bulan yang sisa ganjil ketika dibagi tujuh memiliki 31 hari
    # Untuk mengkompensasi dalam perhitungan sengaja bulan dikurangi satu 
    else:
        return(31 - (((month - 1) % 7) % 2))

# Menentukan urutan hari tanggal tertentu dalam suatu tahun
def dayOfYear(year, month, day):
    if (day < 1 or month < 1 or month > 12 or year < 1):
        return None
    elif day > daysInMonth(year, month):
        return None
    else:
        count = 1
        days = day
        while count < month:
            days += daysInMonth(year, count)
            count += 1
        return days