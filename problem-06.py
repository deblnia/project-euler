def sum_of_squares(end:int)->int:
    ans = 0 
    for x in range(1, end + 1): 
        ans += (x * x)
    return ans

assert sum_of_squares(10) == 385 

def square_of_sum(end:int)->int:
    sum_of_nums = sum([x for x in range(1, end + 1)])
    return sum_of_nums * sum_of_nums 

assert square_of_sum(10) == 3025 


print(square_of_sum(100) - sum_of_squares(100))
