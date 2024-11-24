while True:
    n = int(input("Enter the number of lines: "))
    print("* " * (n + 1))
    for i in range(1, n + 1):
        print("*", " " * (n - 1), "*", " " * (n - 1), "*", sep="")
    print("* " * (n + 1))
    for i in range(n, 0, -1):
        print("*", " " * (n - 1), "*", " " * (n - 1), "*", sep="")
    print("* " * (n + 1))
    key1 = input("ต้องการเริ่มอีกครั้งไหม? (y/n): ")
    while (key1=='N'or key1=='n'or key1=='Y' or key1=='y'):
        if ( key1=='Y' or key1=='y'):
            print("กำลังเริ่มต้นโปรแกรมอีกครั้ง!")            
            break
        else:
            print("ออกจากโปรแกรมเสร็จสิ้น!!!")
            break
    exit()
