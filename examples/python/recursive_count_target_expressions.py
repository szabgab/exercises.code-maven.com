def count_target_expressions(numbers, target):
    # TODO verify that all the numbers and the target are non-negative integers.
    if numbers == []:
        return 0
    if len(numbers) == 1:
        if numbers[0] == target or -lst[0] == target:
            return 1
        else:
            return 0

    return count_target_expressions(numbers[1:], target-lst[0]) + count_target_expressions(lst[1:], target+lst[0])

assert count_target_expressions([0], 1) == 0
assert count_target_expressions([1], 1) == 1

assert count_target_expressions([1, 1, 1, 1, 1], 3) == 5
assert count_target_expressions([2, 3, 5], 0) == 2

