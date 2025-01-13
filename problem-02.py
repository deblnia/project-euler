a, b = 1, 2  
even_sum = 0

while a <= 4_000_000:
    if a % 2 == 0:  
        even_sum += a
    a, b = b, a + b

print("Sum of even Fibonacci numbers:", even_sum)