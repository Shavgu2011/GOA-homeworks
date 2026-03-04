def count_odds(n, use_formula=False):
    if use_formula:
        return (n + 1) // 2
    else:
        count = 0
        for i in range(1, n + 1):
            if i % 2 != 0:
                count += 1
        return count
print(count_odds(10))              
print(count_odds(10, use_formula=True)) 
