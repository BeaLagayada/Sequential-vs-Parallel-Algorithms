import time
from data_generator import load_all_datasets
from sequential_sort import sequential_sort
from parallel_sort import parallel_sort
from sequential_search import sequential_search
from parallel_search import parallel_search


def run_timed(func, *args):
    t0 = time.perf_counter()
    result = func(*args)
    t1 = time.perf_counter()
    return result, round(t1 - t0, 4)


def pick_target(data, mode):
    # pick a target that actually exists so we test a realistic scenario
    if mode == "random":
        return data[len(data) - 1]   # worst case – it's at the end
    return data[len(data) // 2]      # middle for sorted/reverse


def run_all_tests():
    datasets = load_all_datasets()

    print("=" * 75)
    print("SORTING")
    print(f"{'Size':<10} {'Mode':<10} {'Sequential':>14}s  {'Parallel':>12}s  {'Speedup':>8}")
    print("-" * 75)

    for (size, mode), data in datasets.items():
        _, s_time = run_timed(sequential_sort, data)
        _, p_time = run_timed(parallel_sort, data[:])  # copy to be safe
        ratio = round(s_time / p_time, 2) if p_time > 0 else 0
        print(f"{size:<10} {mode:<10} {s_time:>14}   {p_time:>12}   {ratio:>8}")

    print("\n" + "=" * 75)
    print("SEARCHING")
    print(f"{'Size':<10} {'Mode':<10} {'Sequential':>14}s  {'Parallel':>12}s  {'Speedup':>8}")
    print("-" * 75)

    for (size, mode), data in datasets.items():
        target = pick_target(data, mode)
        _, s_time = run_timed(sequential_search, data, target)
        _, p_time = run_timed(parallel_search, data, target)
        ratio = round(s_time / p_time, 2) if p_time > 0 else 0
        print(f"{size:<10} {mode:<10} {s_time:>14}   {p_time:>12}   {ratio:>8}")

    print("\nSpeedup < 1.0 means parallel was actually slower (overhead cost).")


if __name__ == "__main__":
    run_all_tests()