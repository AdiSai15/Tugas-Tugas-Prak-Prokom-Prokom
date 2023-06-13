import tkinter as tk

class rectangle:
    def __init__(self,width,height,center=(0.0,0.0)):
        self.width = width
        self.height = height
        self.center = center
        
    def __repr__(self):
        return "Rectangle(Width={w}, height={h}, center{c})".format(h = self.height, 
                                                                    w = self.width,
                                                                    c = self.center)
    
    def compute_area(self):
        return self.width * self.height
    
    def compute_corners(self):
        cx, cy = self.centerdx 
        dx = self.width / 2.0
        dy = self.height / 2.0
        return [(cx+x,cy+y) for x,y in ((dx,dy), (dx,-dy), (-dx,-dy), (-dx,dy))]
    
    def keliling(self):
        return 2*(self.width + self.height)

class square(rectangle):
    def __init__(self, length, center=(0, 0)):
        super().__init__(length, length, center)

#no 1
kotak1 = rectangle(4,6,0)
ls_kotak1 = kotak1.compute_area()
print(ls_kotak1)  

#no2
kotak2 = rectangle(8,2,0)
ls_kotak2 = kotak2.compute_area()

if ls_kotak1 > ls_kotak2:
    print("Luas Kotak 1 lebih besar dari kotak 2")
elif ls_kotak1 < ls_kotak2:
    print("Luas Kotak 2 lebih besar dari kotak 1")

#no3
k_kotak1 = kotak1.keliling()
k_kotak2 = kotak2.keliling()
print(k_kotak1)
print(k_kotak2)

if k_kotak1 > k_kotak2:
    print("Keliling Kotak 1 lebih besar dari kotak 2")
elif k_kotak1 < k_kotak2:
    print("Keliling Kotak 2 lebih besar dari kotak 1")
    
#no4
kotak1 = rectangle(4,6,0)
ls_kotak1 = kotak1.compute_area()

kotak2 = rectangle(8,2,0)
ls_kotak2 = kotak2.compute_area()

square = square(4)
ls_square = square.compute_area()

if ls_square > ls_kotak1 and ls_square > ls_kotak2:
    print("luas square lebih besar dari kotak 1 dan kotak 2")
elif ls_square > ls_kotak1:
    print("luas square lebih besar dari kotak1")
elif ls_square > ls_kotak2:
    print("luas square lebih besar dari kotak2")
elif (ls_square == ls_kotak1) and (ls_square == ls_kotak2):
    print("luas square sama dengan kotak 1 dan kotak 2")
else:
    print("luas square kurang dari kotak 1 dan kotak 2")