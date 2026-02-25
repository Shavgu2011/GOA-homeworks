numbers = []
for i in range(4):
    num = int(input("შეიყვანე რიცხვი: "))
    numbers.append(num)

if sum(numbers) > 100:
    numbers.clear()

print("საბოლოო სია:", numbers)
