def factorial(n):
    if n<2:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python factorial.py <number>")
        sys.exit(1)
    
    try:
        number = int(sys.argv[1])
        if number < 0:
            raise ValueError("Number must be non-negative.")
        print(f"The factorial of {number} is {factorial(number)}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)