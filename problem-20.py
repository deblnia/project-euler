
def calc_factorial(num: int)->int: 
    total = 1 
    for i in range(1, num + 1):
        total *= i 
    return total 

assert calc_factorial(10) == 3628800

def sum_digits(num: int)->int: 
    total = 0
    for c in str(num):
        total += int(c)
    return total 

assert sum_digits(3628800) == 27

print(sum_digits(calc_factorial(100)))