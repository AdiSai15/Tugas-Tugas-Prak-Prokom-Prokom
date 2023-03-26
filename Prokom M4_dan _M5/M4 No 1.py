
#revisi
A,B = int(input("Masukan Nilai A:")),int(input("Masukan Nilai B:"))
C = A*B
if C<20:
    if A > B:
     A=C
     print(f"A: {A}")
     print(f"B: {B}")
    else:
        A=B
        print(f"A: {A}")
        print(f"B: {B}")
else:
    A,B = int(input("Masukan Nilai A:")),int(input("Masukan Nilai B:"))
    if A > B:
        A=C
        print(f"A: {A}")
        print(f"B: {B}")
    else:
        A=B
        print(f"A: {A}")
        print(f"B: {B}")


