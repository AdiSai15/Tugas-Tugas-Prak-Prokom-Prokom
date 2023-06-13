#Coba Data Diri
class Datadiri:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
x = Datadiri("Painem", 60)
print(x.nama, "Umur", x.umur)

#Coba Data Diri 2
class Datadiri:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def myfunc(self):
        print("Perkenalkan, Nama saya adalah", self.nama, "Umurku", self.umur)
x = Datadiri("Painem", 60)
x.myfunc()
print(x.umur) #opsi aja

#Employee
class Employee:
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)
    
    def displayEmployee(self):
        print ("Name : ", self.name, ", Salary: ", self.salary)

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount) #tidak memanggil displaycount

#Datadiri 3
class Datadiri:
    def __init__(self, namaawal, namaakhir):
        self.nama_awal = namaawal
        self.nama_akhir = namaakhir
    def printnama(self):
        print(self.nama_awal, self.nama_akhir)
y = Datadiri("Christover", "Ivanovski")
y.printnama()

#Datadiri 4
class Datadiri:
    def __init__(self, namaawal, namaakhir):
        self.nama_awal = namaawal
        self.nama_akhir = namaakhir
    def printnama(self):
        print(self.nama_awal, self.nama_akhir)

class Mahasiswa(Datadiri):
    pass

x = Mahasiswa("Christover", "Ivanovski")
x.printnama()