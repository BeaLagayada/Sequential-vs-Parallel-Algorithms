# Sequential vs Parallel Algorithms – Group Project

## Overview
This project implements and compares sequential vs parallel sorting (merge sort) and searching (linear search) using Python's multiprocessing. Datasets: 1k, 100k, 1M elements with random, sorted, and reverse sorted cases.

## How to Run
```bash
python main_runner.py
```

# REFLECTION AND ANALYSIS

## Bea Lagayada
From my perspective as the one running the tests, the biggest difference between sequential and parallel execution came down to speed versus overhead. Parallel versions clearly outperformed sequential ones on large datasets, but for small inputs, the extra cost of creating processes actually made them slower. As the dataset size increased, performance improvements became more noticeable—parallel execution showed significant speedups at 100,000 and especially 1,000,000 elements, while sequential remained more consistent but slower overall. One of the main challenges I faced was integrating different team members’ implementations, especially handling inconsistencies like modifying input data, error handling in empty chunks, and ensuring fair timing measurements. This process also highlighted key insights: overhead is unavoidable in parallel systems, synchronization (like stopping other processes early in search) must be carefully managed, and merging in parallel sort can still become a sequential bottleneck. Overall, parallelism proved most useful for large datasets and early search hits, but unnecessary—or even harmful—for small inputs, late search targets, or systems with limited processing power.


## Mariel Laplap 
Working on sequential (linear) search helped me understand its role as a simple baseline for comparing performance with parallel approaches. I observed that while linear search is efficient for small datasets, its execution time becomes more noticeable as the dataset size increases since it checks each element one by one. Compared to the parallel version, the difference in speed becomes clearer with larger inputs, where dividing the task can reduce overall search time. This experience showed me that although sequential search is straightforward, it is not always the most efficient choice for large-scale problems.