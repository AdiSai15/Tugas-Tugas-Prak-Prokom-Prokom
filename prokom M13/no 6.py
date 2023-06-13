from numpy import *
sdt = [35,2,7.1   ]
print("Besarnya sudut teta dalam satuan DMS adalah:",end=' ')
s = [print(i,end=' ') for i in sdt]
sdt = (sdt[0]+sdt[1]/60+sdt[2]/3600)*(pi/180)
M = array([
    [1/cos(sdt),tan(sdt),-cos(sdt)],
    [sin(sdt),1/tan(sdt),-tan(sdt)],
    [cos(sdt),-sin(sdt),1/sin(sdt)]
    ])
print("\n\nMatrix bujursangkar M adalah:",M,sep='\n')
X = array([[-5],[9],[15]])
print("\nMatriks kolom X adalah:",X,sep='\n')
print("\nMatriks Y = MX adalah:",dot(M,X),sep='\n')
[[]]