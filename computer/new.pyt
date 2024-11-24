num = input("ใส่ตัวเลข: ")
while num.isdigit()== False:
    print("ใส่ตัวเลขไม่ถุกต้อง!!!")
    num = input("ใส่ตัวเลขอีกครั้ง: ")
    
for i in range(num,0,-1):
    print("%2d|" %i)
print("-" * 50)
