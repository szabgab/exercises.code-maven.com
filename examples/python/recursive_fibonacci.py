def fibonacci(n):
    # TODO verify that the parameter is a non-negative integer
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

assert fibonacci(0) == 1
assert fibonacci(1) == 1
assert fibonacci(2) == 2
assert fibonacci(3) == 3
assert fibonacci(4) == 5
assert fibonacci(5) == 8

