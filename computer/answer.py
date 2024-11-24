choice = ['a', 'b', 'c', 'd']
x = int(input("ป้อนจำนวนข้อสอบ: "))
answers = []


print("คำตอบของแต่ละข้อ:")
for i in range(x):
    n = input(f"ข้อที่ {i + 1}: ")
    while n not in choice:
        n = input(f"ข้อที่ {i + 1}: ")    
    answers.append(n)

print("คำตอบของข้อสอบ:", answers)

students = input("จำนวนนักเรียน: ")
while not students.isdigit() or int(students) <= 0:
    students = input("กรุณาป้อนจำนวนนักเรียนเท่านั้น: ")
students = int(students)

student_answers = []
for s in range(students):
    print(f"ป้อนคำตอบของนักเรียน {s + 1}:")
    score = 0
    for i in range(x):
        n = input(f"ข้อที่ {i + 1}: ")
        while n not in choice:
            n = input(f"ข้อที่ {i + 1}: ")
        if n == answers[i]:
            score += 1     
    student_answers.append(score)
    #>---------------------------------------------------
# print("\nตารางดาวตามคะแนน:")
# for i in range(students):
#     print(i+1,end=" ")
#     for j in range(student_answers[i]):
#         print("*",end="")
#     print()
max = 20
for i in range(max,0,-1):
    print("%2d|" %i, end=" ")
    for j in range(students):
        if student_answers[j]>=i:
            print("#",end="  ")
        else:
            print(" ",end="  ")
    print()
#>------------------------------------------------------------
print("   " , end="")
print("-"*50,"เลขที่")
#>---------------------------
print("   ",end="")
for i in range(students):
    print(i+1,end="  ")
    