def count_target_expressions(numbers, target):
    # TODO verify that all the numbers and the target are non-negative integers.
    if not numbers:
        if target == 0:
            return 1
        else:
            return 0

    plus = count_target_expressions(numbers[1:], target-numbers[0])
    minus = count_target_expressions(numbers[1:], target+numbers[0])

    return plus + minus

assert count_target_expressions([], 0) == 1
assert count_target_expressions([], 2) == 0

assert count_target_expressions([0], 1) == 0
assert count_target_expressions([1], 1) == 1

assert count_target_expressions([1, 1, 1, 1, 1], 3) == 5
assert count_target_expressions([2, 3, 5], 0) == 2

