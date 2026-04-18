from multiprocessing import Process, Queue


def search_chunk(sub_data, target, q, offset):
    # scan this slice and report back through the queue
    for local_i, val in enumerate(sub_data):
        if val == target:
            q.put((offset + local_i, True))
            return
    q.put((None, False))  # nothing found here


def parallel_search(data, target, workers=4):
    step = max(1, len(data) // workers)

    slices  = [data[i:i + step] for i in range(0, len(data), step)]
    offsets = [i               for i in range(0, len(data), step)]

    q = Queue()
    procs = []

    for chunk, off in zip(slices, offsets):
        p = Process(target=search_chunk, args=(chunk, target, q, off))
        p.start()
        procs.append(p)

    found_index = -1
    for _ in procs:
        idx, found = q.get()
        if found:
            found_index = idx
            break

    # clean up remaining processes
    for p in procs:
        p.terminate()
        p.join()

    return found_index