
def can_be_written(n:int, pow: int=5)->bool: 
    tmp = 0 
    for c in str(n):
        tmp += (int(c) ** pow)
    return tmp == n 

assert can_be_written(1634, 4)

def find_upper_limit(pow: int)->int: 
    digit_max = 9 ** pow # max given num digits 
    num_digits = 1 
    # largest possible sum of pow-th powers compared to the smallest number with num_digits 
    while num_digits * digit_max >= 10 ** (num_digits - 1):
        num_digits += 1 
    # number of digits * max contribution of any single digit 
    return num_digits * digit_max 

power = 5
upper_limit = find_upper_limit(power)
p30 = 0

for i in range(2, upper_limit):
    if can_be_written(i, power):
        p30 += i

print(p30)