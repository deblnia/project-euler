
from fractions import Fraction
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

def is_wrong_but_right(num:int, denom:int)->bool: 
    num_str, denom_str = str(num), str(denom)

    for digit in num_str:
        if digit in denom_str and digit != '0':  # non-trivial
            new_num = num_str.replace(digit, "", 1)
            new_denom = denom_str.replace(digit, "", 1)
            if new_num and new_denom and new_denom != '0': 
                return (num / denom) == (int(new_num) / int(new_denom))
    return False 

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

assert is_wrong_but_right(49, 98)
assert not is_wrong_but_right(30, 50)
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
wrong_but_right = []
for n in range(10, 100): 
    for d in range(n + 1, 100): # denom > num so fraction is < 1 
        if is_wrong_but_right(n, d): 
            wrong_but_right.append((n, d))

print(wrong_but_right)
assert len(wrong_but_right) == 4 

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
num_prod = 1 
denom_prod = 1 

for n,d in wrong_but_right:
    num_prod *= n 
    denom_prod *= d 
    
print(Fraction(num_prod, denom_prod).denominator)