# Sequential vs Parallel Algorithms – Group Project

## Overview
This project explores the performance differences between sequential and parallel algorithms by implementing both a sorting algorithm (merge sort) and a searching algorithm (linear search) in Python. Using the multiprocessing module, the parallel versions divide the dataset into chunks that are processed concurrently, while the sequential versions handle everything in a single linear flow. Each algorithm is tested across three dataset sizes (1,000, 100,000, and 1,000,000 elements) and three data arrangements (random, sorted, and reverse sorted) to observe how execution time and efficiency change under different conditions. The goal is to understand not just how these algorithms work, but when parallelism actually helps and when it just adds unnecessary overhead.

## How to Run
```bash
python main_runner.py
```

# REFLECTION AND ANALYSIS

## Bea Lagayada
From my perspective as the one running the tests, the biggest difference between sequential and parallel execution came down to speed versus overhead. Parallel versions clearly outperformed sequential ones on large datasets, but for small inputs, the extra cost of creating processes actually made them slower. As the dataset size increased, performance improvements became more noticeable, parallel execution showed significant speedups at 100,000 and especially 1,000,000 elements, while sequential remained more consistent but slower overall. One of the main challenges I faced was integrating different team members’ implementations, especially handling inconsistencies like modifying input data, error handling in empty chunks, and ensuring fair timing measurements. This experience really made it clear that parallel systems come with trade-offs. There’s always some overhead involved, and things like synchronization such as stopping other processes once a result is found, it need to be handled carefully to avoid wasted work. I also noticed that even in parallel sorting, the merging step can slow things down since it still runs sequentially. In the end, parallelism works best when dealing with large datasets or when the target is found early, but it can actually be inefficient for small inputs, late search results, or systems with limited processing power.


## Mariel Laplap 
Working on sequential (linear) search helped me understand its role as a simple baseline for comparing performance with parallel approaches. I observed that while linear search is efficient for small datasets, its execution time becomes more noticeable as the dataset size increases since it checks each element one by one. Compared to the parallel version, the difference in speed becomes clearer with larger inputs, where dividing the task can reduce overall search time. This experience showed me that although sequential search is straightforward, it is not always the most efficient choice for large-scale problems.


## Thomas Gabriel D. Martinez
Working on the sequential search was honestly pretty simple at first since all it does is go through each element one by one until it finds the target. What got interesting was testing it against different dataset sizes. On small data it was fine, but on the 1,000,000 element dataset you could actually feel it slow down, especially when the target was near the end or not there at all. Comparing it to the parallel version was where things got more interesting because on the small dataset the sequential one was actually faster. Spinning up multiple processes and setting up a Queue just to search 1,000 numbers costs more than it saves. The parallel version only started pulling ahead on the larger datasets in worst case scenarios. So the big takeaway for me was that parallel is not always the smarter option, and for something as lightweight as a single comparison, you really need a massive dataset before the extra overhead is worth it.
