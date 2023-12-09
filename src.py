import time

def calculate_execution_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    elapsed_time = end_time - start_time

    return result, elapsed_time

def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)

def iterative_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

numbers_to_test = [0, 5, 10, 15, 20, 25, 30]

for num in numbers_to_test:
    print(f"\nTesting with input {num}:")

    # Test recursive_factorial
    result_recursive, time_recursive = calculate_execution_time(recursive_factorial, num)
    print(f"Factorial (Recursive) of {num}: {result_recursive}")
    print(f"Execution time: {time_recursive} seconds")

    # Test iterative_factorial
    result_iterative, time_iterative = calculate_execution_time(iterative_factorial, num)
    print(f"Factorial (Iterative) of {num}: {result_iterative}")
    print(f"Execution time: {time_iterative} seconds")
