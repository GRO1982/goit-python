def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
if __name__ == '__main__':
    n = int(input("Input n: "))
    print(f"x(n) = {fibonacci(n)}")