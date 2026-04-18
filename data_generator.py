import random

# three ways to build the dataset depending on what we want to test
def build_dataset(n, mode="random"):
    if mode == "random":
        return [random.randint(1, 1_000_000) for _ in range(n)]
    elif mode == "sorted":
        return list(range(1, n + 1))
    elif mode == "reverse":
        return list(range(n, 0, -1))
    else:
        raise ValueError(f"Unknown mode: {mode}. Use 'random', 'sorted', or 'reverse'.")


DATASET_SIZES = {
    "small":  1_000,
    "medium": 100_000,
    "large":  1_000_000,
}

MODES = ["random", "sorted", "reverse"]


def load_all_datasets():
    # returns everything as a dict so main_runner can loop through easily
    all_data = {}
    for label, n in DATASET_SIZES.items():
        for mode in MODES:
            all_data[(label, mode)] = build_dataset(n, mode)
    return all_data