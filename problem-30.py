
def can_be_written(n:int, pow: int=5)->bool: 
    tmp = 0 
    for c in str(n):
        tmp += (int(c) ** pow)
    return tmp == n 

assert can_be_written(1634, 4)

power = 5
# 9 being the largest digit is the terminating condition 
digit_max = 9 ** power
upper_limit = 1
while upper_limit <= digit_max * len(str(upper_limit)):
    upper_limit = upper_limit * 10 + 9  # one more digit just for luck 

p30 = 0
for i in range(2, upper_limit):
    if can_be_written(i, power):
        p30 += i

print(p30)