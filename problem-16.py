
def first_four(num: int, pwr:int): 
    """
    Returns the sum of the digits of the given number raised to the given power 
    """
    tmp_sum = num ** pwr
    digits  = []
    for c in str(tmp_sum): 
        digits.append(int(c))
    return sum(digits)

assert first_four(2, 15) == 26

print(first_four(2, 1000))