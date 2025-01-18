

def len_recurring_cycle(d: int)->int: 
# this should be the long division algo 
    remainders = {}
    remainder = 1 % d 
    pos = 0 

    while remainder != 0: 
        if remainder in remainders: 
            # cycle 
            return pos - remainders[remainder]
        remainders[remainder] = pos 
        # next digit
        remainder = (remainder * 10) % d 
        pos += 1
    return 0 


assert len_recurring_cycle(6) == 1 
assert len_recurring_cycle(7) == 6

# need the value d for which 1/d has a long recurring cycle 
max_len = 0 
curr_max = 0 
for d in range(1, 1000): 
     len_rec = len_recurring_cycle(d)
     if len_rec > max_len: 
          curr_max = d
          max_len = len_rec 

print(curr_max)


