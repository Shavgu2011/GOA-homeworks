numbers = [int(input("რიცხვი: ")) for _ in range(5)]
numbers.sort()
if numbers[0] < 0:
    numbers.clear()
print("სია:", numbers)
