# merge sort – chosen because it splits cleanly for the parallel version later

def combine(left, right):
    merged = []
    a, b = 0, 0

    while a < len(left) and b < len(right):
        if left[a] <= right[b]:
            merged.append(left[a])
            a += 1
        else:
            merged.append(right[b])
            b += 1

    # tack on whatever's left
    merged.extend(left[a:])
    merged.extend(right[b:])
    return merged


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half  = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return combine(left_half, right_half)


def sequential_sort(data):
    return merge_sort(data)