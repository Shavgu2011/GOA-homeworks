person = 0
even = 0
odd = 0
for i in range(0, 6):
    person = int(input("Enter number: "))
    if person % 2 == 0:
        even += 1
    else:
        odd += 1
print(even)
print(odd)