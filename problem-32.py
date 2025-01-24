
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

def is_pandigital(n: int, target:int)->bool: 
    """Returns whether a target number is pandigital up to n"""
    return set(str(target)) == {str(c) for c in range(1, n + 1)}

assert is_pandigital(5, 15234) 

# The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital. 

def test1(): 
    # i'm just combining the multiplicand, multiplier, and product into a string
    combined_num = '391867254'
    if not is_pandigital(9, int(combined_num)):
        return False 
    return True 

assert test1()

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

pandig_nums = set()

# 1-2 digit multiplicand, 3-4 digit multipler means 3-5 digit product and 9 digits total 
for a in range(1, 100):  
    for b in range(a, 5000):  
        product = a * b
        combined = f"{a}{b}{product}"
        if len(combined) > 9:  # Skip if too long
            break
        if len(combined) == 9 and is_pandigital(9, int(combined)):
            pandig_nums.add(product)

result = sum(pandig_nums)
print(f"The sum of all pandigital products is: {result}")




# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.