ans = []
while True:    
    num = input("ป้อนเลข 10-99 เพื่อตรวจสอบ: ")
    while num.isdigit() == False or int(num) > 99 or int(num) < 10 :
        if num.isdigit()==True:
            if int(num)==0:
                break
        num = input("ป้อนเลข 10-99 เพื่อตรวจสอบ: ")
       
#>-------------------------------------------------------------------------
    if int(num)==0:
            break
    if int(num[0]) + int(num[1]) == 10:
        ans.append(num)

print("Result",end=" ")
for i in range(len(ans)):
    print(ans[i],end=" ")
print()
for j in ans:
    print(j)
    