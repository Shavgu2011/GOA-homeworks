def sum_until_zero():
    total = 0
    while True:
        num = int(input("შეიყვანე რიცხვი (0 რომ დასრულდეს): "))
        if num == 0:
            break
        total += num
    return total
result = sum_until_zero()
print("ჯამი არის:", result)
