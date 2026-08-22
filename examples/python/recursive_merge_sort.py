def sort(values):
    if len(values) <= 1:
        return values
    half = int(len(values) / 2)
    left = values[:half]
    right = values[half:]
    left = sort(left)
    right = sort(right)

    sorted_values = []
    i = 0
    j = 0
    while i < len(left) or j < len(right):
        if i >= len(left):
            sorted_values.append(right[j])
            j += 1
            continue
        if j >= len(right):
            sorted_values.append(left[i])
            i += 1
            continue
        if left[i] < right[j]:
            sorted_values.append(left[i])
            i += 1
        else:
            sorted_values.append(right[j])
            j += 1

    return sorted_values

assert sort([1]) == [1]
assert sort([1, 3, 2]) == [1, 2, 3]
assert sort([7, 6, 5, 4, 3, 2, 1, 5]) == [1, 2, 3, 4, 5, 5, 6, 7]
assert sort(["snake", "dog", "mouse", "cat"]) == ["cat", "dog", "mouse", "snake"]


