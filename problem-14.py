
def collatz_len(starting_num: int)->int: 
    """
    Takes in a potential starting number 
    Returns the length of the collatz sequence 
    """
    seq = [] 
    while starting_num != 1: 
        seq.append(starting_num)
        if starting_num % 2 == 0: 
            starting_num = starting_num // 2 
        else:
            starting_num = (3 * starting_num )+ 1  
    seq.append(1)
    return len(seq) 


assert collatz_len(13) == 10


max = 0 
greatest_starting_num = 0 
for i in range(1, 1000000): 
    if collatz_len(i) > max: 
        max = collatz_len(i)
        greatest_starting_num = i
print(greatest_starting_num)



# can memoize to speed things up a big 
def collatz_len(starting_num: int, memo: dict) -> int:
    """
    Takes in a potential starting number and a memoization dictionary.
    Returns the length of the Collatz sequence.
    """
    if starting_num in memo:
        return memo[starting_num]
    
    if starting_num == 1:
        return 1
    
    if starting_num % 2 == 0:
        next_num = starting_num // 2
    else:
        next_num = 3 * starting_num + 1
    
    length = 1 + collatz_len(next_num, memo)
    memo[starting_num] = length
    return length    