numbers = [int(input("რიცხვი: ")) for _ in range(6)]
count_10 = numbers.count(10)
if count_10 > 2:
    numbers.remove(10)
print("რიცხვი 10 რამდენჯერ გვხვდება:", count_10)
print("სია:", numbers)
