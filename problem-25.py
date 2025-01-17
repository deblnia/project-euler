# from functools import lru_cache

# without this, this takes forever 
# @lru_cache(maxsize=None)
# def fib(n: int)->int: 
#     """
#     Returns the nth fibonacci number 
#     """
#     if n <= 1: 
#         return n 
#     return fib(n - 1) + fib(n - 2)
    # could also do this iteratively 
    # a, b = 0, 1
    # for i in range(0, n):
    #     a, b = b, a + b
    # return a
    # or analytically? https://artofproblemsolving.com/wiki/index.php/Binet%27s_Formula?srsltid=AfmBOor0VMNNHVH6wRs6DXPj4wkhIUzgngYSwFegJR11k1fxYrN7JQou


# assert fib(12) == 144

def memoized_fib(n: int, memo:dict={0: 0, 1:1})->int: 
    """
    Returns the nth fibonacci number efficiently 
    """
    if n not in memo: 
        memo[n] = memoized_fib(n - 1, memo) +  memoized_fib(n - 2, memo)
    return memo[n]

assert memoized_fib(12) == 144

i = 0 
while True: 
    if len(str(memoized_fib(i))) == 1000: 
        print(i)
        break  
    else: 
        i += 1 