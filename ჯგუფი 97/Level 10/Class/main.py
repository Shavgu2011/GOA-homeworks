# nums = [10, 20, 30, 40, 50, 3, 4, 5, 6, 6]

# print(len(nums))




# chars = ['a' , 'b' , 'c']

# print(chars[-1])
# print(chars[-2])
# print(chars[-3])



# thislist = ['apple' , 'banana' , 'cherry' , 'orange', 'kiwi' , 'melon' , 'mango']

# print(thislist[2:5])



# thislist = ['apple' , 'banana' , 'cherry' , 'orange', 'kiwi' , 'melon' , 'mango']


# print(thislist[-4:5])
# print(thislistp[:4])
# print(thislist[1:])




# thislist = ['apple' , 'banana', 'cherry']

# if 'apple' in thislist:
#     print("Yes, apple is in the fruits list ")



# thislist = ['Orange', 'Banana', 'Python']

# for i in thislist:
#     print(str(1) + ' ' + i)




# thislist = ['Orange', 'Banana', 'Python']

# for i in range(len(thislist)):
#     print(thislist[i])



# thislist = ['Orange', 'Banana', 'Python']


# print(thislist[2][1])

# thislist[2][1] = 'a'

# print(thislist)




# thislist = ['Orange', 'Banana', 'Python']

# temp_list = list(thislist[2])

# temp_list[1] = 'a'

# thislist[2] = "". join(temp_list)


# print(thislist)






# thislist = ['Orange', 'Banana', 'Python']

# i = 0

# while i < len(thislist):
#     print(thislist[i])
#     i += 1



# nums = [10, 20, 30]

# for i in nums:
#     if len(nums) < 4:
#         nums.append(100)


# print(nums)

# nums = [10, 20, 30]

# strings = ['a' , 'b', 'c']

# nums.append(strings)

# print(nums)



# x = [1, 2, 3, 4, 5]

# for i in x:
#     if len(x) > 3:
#         x.clear()

# print(x)





# chars = ['a', 'b', 'c', 'd', 'e']

# x = chars.copy()


# if chars == x:
#     print('List is copied')





# nums = [5, 10, 15, 5, 25, 10, 12, 12, 5]


# x = nums.count(15)


# print(x)

# fruits = ['apple' , 'cherry', 'kiwi']

# fruits.remove('kiwi')

# print(fruits)


# fruits = ['apple' , 'cherry', 'kiwi']

# if 'cherry' in fruits:
#     print('in list, we have value named cherry, so we will remove it')
#     fruits.remove('cherry')
#     print(fruits)
# else:
#     print('there is no value named cherry')

# bools = [True, False, 10.44]

# bools.pop(0)

# print(bools)


# bools = [True, False, 10.44]

# removed_item = bools.pop(1)

# print(removed_item)



# nums = [100, 200, 300, 400]

# nums.reverse()

# print(nums)

# cars = ['Ford', 'Nissan', 'bmw', 'mercedes', 'byd']

# cars.sort()
# print(cars)

cars = ['Ford', 'Nissan', 'bmw', 'mercedes', 'byd']
# nums = [12, 31, 232, 122, 44, 99, 11, 87]

cars.sort(reverse=True)

print(cars)