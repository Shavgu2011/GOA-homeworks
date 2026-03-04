def sum_to_n(n, use_formula=False):
    if use_formula:
        return n * (n + 1) // 2
    else:
        total = 0
        for i in range(1, n + 1):
            total += i
        return total
print(sum_to_n(5))              
print(sum_to_n(5, use_formula=True))  




