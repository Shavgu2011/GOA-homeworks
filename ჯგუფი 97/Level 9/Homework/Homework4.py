numbers = [0]*5   

for i in range(5):
    numbers[i] = int(input("Enter numbers: "))

total = 0
for num in numbers:
    total += num

print("რიცხვების სია:", numbers)
print("რიცხვების ჯამი არის:", total)