# def is_evenly_divisible(num: int, arr: list[int]) -> bool: 
#     for x in arr: 
#         if num % x != 0: 
#             return False 
#     return True 

# def solve(num: int) -> int:
#     divisors = [x for x in range(1, 21)] 
#     while True:
#         if is_evenly_divisible(num, divisors):
#             print(num)
#             return num
#         num += 20  # num must be a multiple of 20 

# solve(20)

# more efficient - log time - but also more mathy solution 
from math import gcd
from functools import reduce

def lcm(a, b):
    return a * b // gcd(a, b)

def solve():
    # Find LCM of numbers from 1 to 20
    return reduce(lcm, range(1, 21))

print(solve())