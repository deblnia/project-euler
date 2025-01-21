
def generate_sequence_len(lower:int, upper:int)->int: 
    # could also be a one liner 
    # return len({a ** b for a in range(lower, upper + 1) for b in range(lower, upper + 1)})

    seq = set()
    for a in range(lower, upper + 1): 
        for b in range(lower, upper+1):
            seq.add(a ** b)
    return len(list(seq))

assert generate_sequence_len(2, 5) == 15

print(generate_sequence_len(2, 100))