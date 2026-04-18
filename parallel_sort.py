from multiprocessing import Pool
from sequential_sort import sequential_sort   # reuse the merge sort

def sort_chunk(chunk):
    return sequential_sort(chunk)

def parallel_sort(data, num_processes=4):
    """Parallel merge sort: split, sort each chunk, then merge."""
    if len(data) < 1000:   # small fallback
        return sequential_sort(data)
    
    chunk_size = max(1, len(data) // num_processes)
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    
    with Pool(processes=num_processes) as pool:
        sorted_chunks = pool.map(sort_chunk, chunks)
    
    # Merge sorted chunks sequentially
    result = []
    for chunk in sorted_chunks:
        result = merge(result, chunk)   # reuse merge from sequential_sort
    return result

# We need the merge function (copy or import). For independence, we can define it here.
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result