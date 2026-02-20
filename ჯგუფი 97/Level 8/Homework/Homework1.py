num = 0
pluse = 0
minus = 0
for i in range(0, 5):
    num = int(input("Enter number: "))
    if num > 0:
        pluse += 1
    elif num == 0:
        num = num
    else:
        minus += 1
print(pluse)
print(minus)