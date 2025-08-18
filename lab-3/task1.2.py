def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result

def main():
    try:
        n = int(input("Enter a non-negative integer: "))
        print(f"Factorial of {n} is {factorial(n)}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()