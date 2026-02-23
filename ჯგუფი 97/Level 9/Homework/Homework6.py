numbers = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]

print("საწყისი სია:", numbers)

count = 0
for i in range(len(numbers)):
    if numbers[i] % 2 != 0:   
        count += 1

print("კენტი რიცხვების რაოდენობა არის:", count)