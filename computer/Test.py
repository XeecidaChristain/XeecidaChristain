 
money = int(input("กรอกจำนวนเงินที่ต้องการแลกเปลี่ยน : "))
money_type = [1000, 500, 100, 50, 20, 10]
 
for t in money_type:
    if money >= t:
        print("{} บาท = {}".format(t, int(money / t)))
        money = money % t