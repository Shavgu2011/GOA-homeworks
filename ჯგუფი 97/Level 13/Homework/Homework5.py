def filter_even(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens
print(filter_even([1, 2, 3, 4, 5, 6]))  
