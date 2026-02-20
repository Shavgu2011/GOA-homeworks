person = 0
num = 0
for i in range(0, 5):
    person = int(input("Enter number: "))
    if person > num:
        num = person
print(num)