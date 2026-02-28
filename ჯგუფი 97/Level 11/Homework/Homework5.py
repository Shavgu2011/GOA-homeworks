numbers = [int(input("რიცხვი: "))for _ in range(7)]
numbers.sort()
max_num = max(numbers)
count_max = numbers.count(max_num)
numbers.remove(max_num)
print("მაქსიმალური რიცხვი რამდენჯერ გვხვდება:", count_max)
print("სია:", numbers)