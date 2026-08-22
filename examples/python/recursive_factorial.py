def factorial(n):
    # TODO make sure the function receives a non-negative integer
    if n == 0:
        return 1
    return n * factorial(n-1)

assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(2) == 2
assert factorial(3) == 6
assert factorial(4) == 24
