# Sequential vs Parallel Algorithms – Group Project

## Overview
This project explores the performance differences between sequential and parallel algorithms by implementing both a sorting algorithm (merge sort) and a searching algorithm (linear search) in Python. Using the multiprocessing module, the parallel versions divide the dataset into chunks that are processed concurrently, while the sequential versions handle everything in a single linear flow. Each algorithm is tested across three dataset sizes (1,000, 100,000, and 1,000,000 elements) and three data arrangements (random, sorted, and reverse sorted) to observe how execution time and efficiency change under different conditions. The goal is to understand not just how these algorithms work, but when parallelism actually helps and when it just adds unnecessary overhead.

## How to Run
```bash
python main_runner.py
```
---

# REFLECTION AND ANALYSIS

## Roger Bao  Jr.
Working through the parallel merge sort implementation made it clear just how differently sequential and parallel execution approach the same problem. Sequential sorting follows a straightforward recursive flow, while parallel sorting breaks data into chunks, processes them simultaneously, and merges them at the end. Performance-wise, parallel sorting wasn't automatically better since for small inputs, process overhead actually made it slower, and the speedups only became noticeable around 100,000 to 1,000,000 elements. The trickiest part was merging sorted chunks efficiently without losing the gains from parallelism, and knowing when not to parallelize was just as important as knowing when to. Overall, parallelism earns its keep on large datasets and multi-core systems, but for small inputs or resource-constrained environments, it's more trouble than it's worth.

## Bea Lagayada
From my perspective as the one running the tests, the biggest difference between sequential and parallel execution came down to speed versus overhead. Parallel versions clearly outperformed sequential ones on large datasets, but for small inputs, the extra cost of creating processes actually made them slower. As the dataset size increased, performance improvements became more noticeable, parallel execution showed significant speedups at 100,000 and especially 1,000,000 elements, while sequential remained more consistent but slower overall. One of the main challenges I faced was integrating different team members’ implementations, especially handling inconsistencies like modifying input data, error handling in empty chunks, and ensuring fair timing measurements. This experience really made it clear that parallel systems come with trade-offs. There’s always some overhead involved, and things like synchronization such as stopping other processes once a result is found, it need to be handled carefully to avoid wasted work. I also noticed that even in parallel sorting, the merging step can slow things down since it still runs sequentially. In the end, parallelism works best when dealing with large datasets or when the target is found early, but it can actually be inefficient for small inputs, late search results, or systems with limited processing power.


## Mariel Laplap 
Working on sequential (linear) search helped me understand its role as a simple baseline for comparing performance with parallel approaches. I observed that while linear search is efficient for small datasets, its execution time becomes more noticeable as the dataset size increases since it checks each element one by one. Compared to the parallel version, the difference in speed becomes clearer with larger inputs, where dividing the task can reduce overall search time. This experience showed me that although sequential search is straightforward, it is not always the most efficient choice for large-scale problems.


## Thomas Gabriel D. Martinez
My part in this project was handling the sequential search, which turned out to be a good way to understand how a simple algorithm behaves under pressure. The logic itself is nothing complicated, just checking each element in order until the target shows up or the list runs out. Testing it across different sizes is where it got more revealing. Smaller datasets finished without any issues, but once the list hit 1,000,000 elements and the target was sitting at the end or missing completely, the slowdown was obvious. Stacking it up against the parallel version showed something I did not expect at first, which was that sequential actually won on the small dataset. The cost of creating processes, splitting the data, and coordinating through a Queue simply was not worth it for 1,000 elements. The parallel version only started making sense on the larger datasets where the workload was heavy enough to justify all that setup. The lesson I got from this is that more complexity does not always mean better performance, and for a task as quick as a single comparison, parallelism only becomes useful when the scale is large enough to absorb the extra cost.
