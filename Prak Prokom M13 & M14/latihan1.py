#NO4
#sisi
#input panjang sisi
sisi_1 = int(input("Panjang sisi 1:"))
sisi_2 = int(input("Panjang sisi 2:"))
sisi_3 = int(input("Panjang sisi 3:"))

if sisi_1 == sisi_2 == sisi_3:
    print("Merupakan segitiga sama sisi")
elif (sisi_1 == sisi_2) or (sisi_2 == sisi_3) or (sisi_1 == sisi_3):
    print("Merupakan segitiga sama kaki")
else :
    print("Merupakan segitiga sembarang")

#sudut
sdt1 = int(input("Besar sudut 1:"))
sdt2 = int(input("Besar sudut 2:"))
#sdt3 = int(input("Besar sudut 3:"))

if (sdt1<90) and (sdt2<90):
    print("Merupakan segitiga tumpul")
elif ((sdt1<90) and (sdt2>90)) or ((sdt1>90) and (sdt2>90)):
    print("Merupakan segitiga siku-siku")
else:
    print("Merupakan segitiga lancip")
    
#NO5
X = 1
while X <= 11:
    print('')
    print(X, end=' ')
    Y = 1
    while Y <=11:
        print(X*Y, end=' ')
        Y+=1
    X+=1
