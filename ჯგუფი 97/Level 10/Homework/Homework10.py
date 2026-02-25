numbers = []
for i in range(6):
    num = int(input("შეიყვანე რიცხვი: "))
    numbers.append(num)

count_five = numbers.count(5)
print("რიცხვი 5 გვხვდება", count_five, "ჯერ")

if count_five > 0:
    numbers.remove(5)

print("საბოლოო სია:", numbers)
