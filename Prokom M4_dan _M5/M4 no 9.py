# input jumlah pecahan
n = int(input("Masukkan jumlah pecahan: "))
sum = 0
# loop untuk menghitung jumlah pecahan
for i in range(1, n):
    sum += 1/(i+1)
    print(f"{i}/{i+1}", end=" + ")
sum+=n/(n+1)
print(f"{n}/{n+1} = {sum}")
