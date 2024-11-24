
text = input("ป้อนตัวอักษร: ")
print(len(text))
x = text.split()#split คือฟังกืชั่นแยกคำ
#print(x)
text = "".join(x)#join คือฟังก์ชั่น ร่วมเข้าด้วยกัน
#print(text)
text2 = list(dict.fromkeys(text))# dict คือฟังก์ชั่นเป็นตัวชี้ข้อความ
#print(text2)
#for i in text:
#    print(i)
for i in text2:
    print(i,end="=")
    n = 0
    for j in text:
        if i == j:
            n +=1
    print(n)