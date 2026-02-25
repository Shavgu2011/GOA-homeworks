numbers = []

for i in range(5):
    num = int(input("შეიყვანე რიცხვი: "))
    numbers.append(num)

numbers.sort()

largest = numbers.pop()  

print("ყველაზე დიდი რიცხვი იყო:", largest)
print("საბოლოო სია:", numbers)
