import time
from data_generator import get_all_datasets, SIZES, CASES
from sequential_sort import sequential_sort
from parallel_sort import parallel_sort
from sequential_search import sequential_search
from parallel_search import parallel_search

def measure_time(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    return result, end - start

def run_all_tests():
    datasets = get_all_datasets()
    
    print("="*80)
    print("SORTING PERFORMANCE")
    print(f"{'Size':<10} {'Case':<12} {'Sequential (s)':<18} {'Parallel (s)':<18} {'Speedup':<10}")
    print("-"*80)
    
    for (size_name, case), data in datasets.items():
        # Sequential sort
        _, seq_time = measure_time(sequential_sort, data)
        # Parallel sort (copy data to avoid accidental modification)
        _, par_time = measure_time(parallel_sort, data.copy())
        speedup = seq_time / par_time if par_time > 0 else 0
        print(f"{size_name:<10} {case:<12} {seq_time:<18.4f} {par_time:<18.4f} {speedup:<10.2f}")
    
    print("\n" + "="*80)
    print("SEARCHING PERFORMANCE (target = middle value or last element)")
    print(f"{'Size':<10} {'Case':<12} {'Sequential (s)':<18} {'Parallel (s)':<18} {'Speedup':<10}")
    print("-"*80)
    
    for (size_name, case), data in datasets.items():
        # Choose a target that exists (for random, pick the first element; for sorted/reverse, pick middle)
        if case == "random":
            target = data[0]   # exists
        elif case == "sorted":
            target = data[len(data)//2]
        else:  # reverse
            target = data[len(data)//2]
        
        # Sequential search
        _, seq_time = measure_time(sequential_search, data, target)
        # Parallel search
        _, par_time = measure_time(parallel_search, data, target)
        speedup = seq_time / par_time if par_time > 0 else 0
        print(f"{size_name:<10} {case:<12} {seq_time:<18.4f} {par_time:<18.4f} {speedup:<10.2f}")
    
    print("\nNote: Negative speedup (<1) means parallel was slower due to overhead.")

if __name__ == "__main__":
    run_all_tests()