def sort(values):
    if len(values) <= 1:
        return values
    first = values[0]
    rest = values[1:]
    sorted_values = sort(rest)
    for i in range(len(sorted_values)):
        if first < sorted_values[i]:
            sorted_values.insert(i, first)
            return sorted_values
    sorted_values.append(first)
    return sorted_values

assert sort([1]) == [1]
assert sort([1, 3, 2]) == [1, 2, 3]
assert sort([7, 6, 5, 4, 3, 2, 1, 5]) == [1, 2, 3, 4, 5, 5, 6, 7]
assert sort(["snake", "dog", "mouse", "cat"]) == ["cat", "dog", "mouse", "snake"]

