numbers = [int(input("რიცხვი: ")) for _ in range(4)]
copy_numbers = numbers.copy()
copy_numbers.append(100)
copy_numbers.reverse()
print("საწყისი სია:", numbers)
print("კოპირებული სია:", copy_numbers)
