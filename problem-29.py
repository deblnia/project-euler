
def generate_sequence_len(lower:int, upper:int)->int: 
    seq = set()
    for a in range(lower, upper + 1): 
        for b in range(lower, upper+1):
            seq.add(a ** b)
    return len(list(seq))

assert generate_sequence_len(2, 5) == 15

print(generate_sequence_len(2, 100))