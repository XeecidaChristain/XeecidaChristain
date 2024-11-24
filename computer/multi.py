# number = 10
x = input('ป้อนตัวเลข: ') 
while not(x.isdigit()) : #เช็คว่าเป็นตัวเลขหรือไม่ 
    x = input('ป้อนตัวเลข: ')
x= int(x) #แปลงตัวอักษรเป็นตัวเลข


for x in range(1,x+1):
    for j in range(1,13):
        print("%3d" %(x * j),end=" " )
    print()
    
