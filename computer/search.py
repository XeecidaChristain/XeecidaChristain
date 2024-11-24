num = []
while True:
    search = input("Enter Number: ")
    while search.isdigit() == False:
        print("กรอกเลขไม่ถูกต้องกรุณากรอกใหม่อีกครั้ง!")
        search = input("Enter Number: ")
    if int(search) == 0:
        break
    while int(search) > 99 or int(search) < 1:
        print("ป้อนเลขไม่ถูกต้องและห้ามเกิน 99 และต่ำกว่า 1")
        search = input("Enter Number: ")
    if int(search) == 0:
        break
    num.append(int(search))
#num.sort()#>sort = เรียงลำดับจากน้อยไปหามาก    
print()
#------------------------------------------
for i in range(len(num)):
    for j in range(len(num)):
        if num[j] > num[i]:
            print(f"num[{j}] ={num[j]}  num[{i}]={num[i]}")
            temp=num[j]
            num[j]=num[i]
            num[i]=temp
            print(f"==>num{j}={num[j]} num{i}={num[i]}")
#---------------------------------------
print("Result", end=" ")
for i in range(len(num)):
    print(num[i], end=" ")
found=False
indx=input("\nFound index:")
#-------------------------------------
#-------------------------------------
indx=int(indx)

for i in range(len(num)):
    if indx==num[i]:
        found=True
        indx2=i+1
    
if found==True:
    print(f"Found index:{indx2} ")
else:
    print(f"Not Found!!! ")
        
