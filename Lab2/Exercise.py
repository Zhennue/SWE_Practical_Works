def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Test the function
for i in range(10):
    print(f"F({i}) = {fibonacci_recursive(i)}")

def fibonacci_iterative(n):
    if n < 0:
        return []
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[:n]

# Test the function
n = 10
fib_list = fibonacci_iterative(n)
print(f"Fibonacci numbers up to F({n}) = {fib_list}")

def fibonacci_exceeds(value):
    a, b = 0, 1
    index = 0
    while a <= value:
        a, b = b, a + b
        index += 1
    return index

# Test the function
value = 20
index = fibonacci_exceeds(value)
print(f"The first Fibonacci number that exceeds {value} is at index: {index}")

def is_fibonacci_number(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

# Test the function
num = 13
is_fib = is_fibonacci_number(num)
print(f"{num} is a Fibonacci number: {is_fib}")

def fibonacci_ratio(limit):
    ratios = []
    a, b = 0, 1
    for _ in range(2, limit):
        a, b = b, a + b
        if a != 0:
            ratios.append(b / a)
    return ratios

# Test the function
ratios = fibonacci_ratio(10)
print(f"Ratios between consecutive Fibonacci numbers: {ratios}")

# Bonus: Check how the ratio approaches the golden ratio
golden_ratio = (1 + 5**0.5) / 2
print(f"Golden ratio: {golden_ratio:.6f}")