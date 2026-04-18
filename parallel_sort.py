from multiprocessing import Pool
from sequential_sort import sequential_sort, combine


def sort_piece(piece):
    # each worker just runs the sequential sort on its chunk
    return sequential_sort(piece)


def parallel_sort(data, workers=4):
    # not worth spawning processes for tiny lists
    if len(data) < 1000:
        return sequential_sort(data)

    step = max(1, len(data) // workers)
    pieces = [data[i:i + step] for i in range(0, len(data), step)]

    with Pool(processes=workers) as pool:
        sorted_pieces = pool.map(sort_piece, pieces)

    # merge all sorted chunks back into one list
    final = []
    for piece in sorted_pieces:
        final = combine(final, piece)

    return final