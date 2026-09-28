def reverse_array(arr):
    return arr[::-1]


def count_values(arr):
    counts = {}
    for value in arr:
        counts[value] = counts.get(value, 0) + 1
    return counts


def find_max(arr):
    if not arr:
        raise ValueError("Array cannot be empty.")
    maximum = arr[0]
    for value in arr[1:]:
        if value > maximum:
            maximum = value
    return maximum


def remove_duplicates(arr):
    result = []
    seen = set()
    for value in arr:
        if value not in seen:
            result.append(value)
            seen.add(value)
    return result


def kth_smallest(arr, k):
    if not arr:
        raise ValueError("Array cannot be empty.")
    if k < 1 or k > len(arr):
        raise ValueError("k must be between 1 and the array length.")
    return sorted(arr)[k - 1]


def partition_array(arr, pivot):
    less, equal, greater = [], [], []
    for value in arr:
        if value < pivot:
            less.append(value)
        elif value == pivot:
            equal.append(value)
        else:
            greater.append(value)
    return less, equal, greater
