
def find_proper_divisors(num: int)->list: 
    div = []
    # can iterate to square root to make this more efficient for ex: 
    # divisors = [1]
    # for i in range(2, int(num**0.5) + 1):
    #     if num % i == 0:
    #         divisors.append(i)
    #         if i != num // i:  # avoid adding the square root twice
    #             divisors.append(num // i)
    # return divisors
    for i in range(1, num):
        if num % i == 0: 
            div.append(i)
    return div 

def d(n: int) -> int: 
    return sum(find_proper_divisors(n))

def is_amicable(a:int) -> bool:
    b = d(a)
    return b != a and d(b) == a


assert find_proper_divisors(220) == [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
assert d(220) == 284
assert is_amicable(220)

amicable_numbers = set()
for i in range(1, 10000):
    if is_amicable(i):
        amicable_numbers.add(i)

print(sum(amicable_numbers))
