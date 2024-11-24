mul=[1,2,3,4,5,6,7,8,9,10,11,12]
x = input('ป้อนตัวเลข: ') 
while not(x.isdigit()) : #isdigit เช็คว่าเป็นตัวเลขหรือไม่ 
    x = input('ป้อนตัวเลข: ')
x= int(x) #แปลงตัวอักษรเป็นตัวเลข

for i in range(1,x+1):
    for j in mul:
        print("%3d" %(x * j),end=" " )
    print()    