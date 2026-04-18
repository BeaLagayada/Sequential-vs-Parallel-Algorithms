import time

def sequential_search(data, target):
    found = False
    idx = -1

    # go through each element, stop as soon as we find it
    for i in range(len(data)):
        if data[i] == target:
            found = True
            idx = i
            break  # early exit, no need to keep scanning

    return idx  # returns -1 if never found


def timed_sequential_search(data, target):
    t0 = time.perf_counter()
    result = sequential_search(data, target)
    t1 = time.perf_counter()
    elapsed = round(t1 - t0, 6)
    return result, elapsed