def is_even(n): 
    if n % 2 == 0:
        return True
    else:
        return False
    
def main (verb, noun):
    return verb + noun

def even_or_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

def number_to_string(num):
    return str(num)

def boolean_to_string(b):
    if b > 10:
        return str(b)
    else:
        return str(b)
    
def say_hello(name):
    return f"Hello, {name}"

def quarter_of(month):
    return (month - 1) // 3 + 1