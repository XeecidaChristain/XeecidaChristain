def money(amount):
    m = [100,50,20,10]
    result = {}
    
    for n in m:
        if amount > n:
            result[f'N{n}'] = amount // n
            amount %= n
        else:
            result[f'N{n}'] = 0

    return result
#------------------------------------------------------------------------------------------------
try:
    result = int(input("กรุณาใส่จำนวนเงินที่ต้องการแลก (100, 500, 1000): "))
    if result not in [100,500,1000]:
        print("กรุณาใส่จำนวนเงินที่ถูกต้อง (100, 500, 1000 บาท)")
    else:
        result = money(result)
        print("\nผลลัพธ์:")
        for denom, count in result.items():
            print(f"{denom}: {count}")
except ValueError:
    print("กรุณาใส่ตัวเลขจำนวนเงินที่ถูกต้อง")
    