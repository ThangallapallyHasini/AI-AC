def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage:
terms = 10
print(f"Fibonacci sequence up to {terms} terms:")
print(fibonacci(terms))