password = input("Enter your password: ")
real_password = ("2130")
num = 12
while num != 0:
    if password != real_password:
        password = input("Try again: ")
    elif password == real_password:
        num -= 12
print("Right password! ")