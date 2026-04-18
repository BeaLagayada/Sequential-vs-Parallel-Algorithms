from multiprocessing import Process, Queue

def worker(sub_data, target, q, offset):
    """Search sub_data for target; put (found_index, global_index) into queue."""
    for local_idx, val in enumerate(sub_data):
        if val == target:
            q.put((offset + local_idx, True))
            return
    q.put((None, False))   # not found in this chunk

def parallel_search(data, target, num_processes=4):
    """Return first global index of target, or -1 if not found."""
    chunk_size = max(1, len(data) // num_processes)
    chunks = []
    offsets = []
    for i in range(0, len(data), chunk_size):
        chunks.append(data[i:i+chunk_size])
        offsets.append(i)
    
    q = Queue()
    processes = []
    for chunk, off in zip(chunks, offsets):
        p = Process(target=worker, args=(chunk, target, q, off))
        p.start()
        processes.append(p)
    
    result_index = -1
    for _ in processes:
        idx, found = q.get()
        if found:
            result_index = idx
            break   # we have the first occurrence (lowest index)
    
    # Terminate all processes after first result
    for p in processes:
        p.terminate()
        p.join()
    
    return result_index