

def is_curious(n:int)->bool:
    # curious number is sum of factorials of digits 
    ns = str(n)
    s = 0 
    for d in ns: 
        tmp_prod = 1 
        for i in range(1, int(d) + 1): 
            tmp_prod *= i
        s += tmp_prod 
    return s == n

assert is_curious(145) 

# the tricky part is finding the end condition 
# that's usually something math-y or analytic 
nums = []
for n in range(3, 2000000): 
# tbh just picked an arbitrarily big number 
# from web: 
    # for a num with d digits, the max sum of digits is d * 9! 
    # if d * 9! is smaller than the smallest d digit number,
    # it can't be curious! 
    if is_curious(n):
        nums.append(n) # could also precompute this, but it reasonable as is 
print(nums) 
print(sum(nums)) 
