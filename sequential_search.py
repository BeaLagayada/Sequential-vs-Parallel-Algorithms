def sequential_search(data, target):
    """Return first index of target, or -1 if not found."""
    for i, val in enumerate(data):
        if val == target:
            return i
    return -1