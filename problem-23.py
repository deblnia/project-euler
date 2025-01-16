
def get_proper_divisors_sum(n:int)->int: 
    """
    Returns the sum of the proper divisors of a given number 
    """
    div = [1]
    for i in range(2, int(n ** 0.5 + 1)): # divisors come in pairs so only need up to sqrt
        if n % i == 0: # perfect divisor: 
            div.append(i)
            if i != (n // i): # don't add the sqrt twice 
                div.append(n // i) # but add pair otherwise 
    return sum(div)

assert get_proper_divisors_sum(28) == 28

def is_abundant(n: int)->bool: 
    """
    Returns a boolean indicating whether the given number is abundant or not 
    """
    return get_proper_divisors_sum(n) > n

assert is_abundant(12)

def get_abundant_nums(limit: int)->list[int]: 
    """
    Returns a list of all abundant nums up (NOT INCLUDING) to a given limit 
    """
    return [x for x in range(1, limit) if is_abundant(x)]

assert get_abundant_nums(24) == [12, 18, 20]

def get_non_summable_numbers(limit: int)->list[int]: 
    """
    
    """
    abundant = get_abundant_nums(limit)
    abundant_sums = set()

    # need all possible sums of abundant numbers 
    for i in abundant: 
        for j in abundant: 
            if i + j < limit: 
                abundant_sums.add(i + j)
            else: break 
    return [n for n in range(1, limit) if n not in abundant_sums]

limit = 28124
non_summable_numbers = get_non_summable_numbers(limit)
result = sum(non_summable_numbers)
print(result)