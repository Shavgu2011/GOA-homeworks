person = int(input("Enter number: "))
num = 12
while num != 0:
    if person <= 0:
        person = int(input("Try again: "))
    else:
        print('Right number')
        num -= 12