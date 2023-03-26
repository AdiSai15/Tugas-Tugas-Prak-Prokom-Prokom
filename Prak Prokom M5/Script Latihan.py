#Program Belah Ketupat
X = int(input('Lebar: '))
for k in range(X):
  print(' ' * (X-k),end='')
  print('+ ' * (k+1))
   
for j in range(1,X):
  print(' ' * (j+1),end='')
  print('+ ' * (X-j))
  
#program nomor 1 k,l,m (program belah ketupat berbeda )
x,y = int(input('Masukan nilai Lebar:')), int(input('Masukan nilai Panjang:'))
for k in range(x):
    for l in range(x-k):
        print(' ', end='')
    for l in range(k+1):
        print('+ ', end='')
    print()
for k in range(x-1):
    for l in range(k+2):
        print(' ', end='')
    for l in range(x-k-1):
        print('+ ', end='')
    print()
