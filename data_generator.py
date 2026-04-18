import random

def generate_dataset(size, case="random"):
    """Generate a list of integers of given size.
    case: 'random', 'sorted', 'reverse'
    """
    if case == "random":
        data = [random.randint(1, 1_000_000) for _ in range(size)]
    elif case == "sorted":
        data = list(range(1, size + 1))
    elif case == "reverse":
        data = list(range(size, 0, -1))
    else:
        raise ValueError("case must be 'random', 'sorted', or 'reverse'")
    return data

# Predefined dataset sizes
SIZES = {
    "small": 1_000,
    "medium": 100_000,
    "large": 1_000_000
}

CASES = ["random", "sorted", "reverse"]

def get_all_datasets():
    """Returns a dict: {(size_name, case): data_list}"""
    datasets = {}
    for size_name, n in SIZES.items():
        for case in CASES:
            datasets[(size_name, case)] = generate_dataset(n, case)
    return datasets