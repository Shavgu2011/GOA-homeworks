numbers = [int(input("რიცხვი: ")) for _ in range(5)]

numbers.sort()

smallest = numbers.pop(0)

print("ამოღებული რიცხვი:", smallest)
print("დარჩენილი სია:", numbers)

