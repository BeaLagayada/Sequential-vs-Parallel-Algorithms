# Sequential vs Parallel Algorithms – Group Project

## Overview
This project implements and compares sequential vs parallel sorting (merge sort) and searching (linear search) using Python's multiprocessing. Datasets: 1k, 100k, 1M elements with random, sorted, and reverse sorted cases.

## How to Run
```bash
python main_runner.py
```

# REFLECTION AND ANALYSIS

## Mariel Laplap 
Working on sequential (linear) search helped me understand its role as a simple baseline for comparing performance with parallel approaches. I observed that while linear search is efficient for small datasets, its execution time becomes more noticeable as the dataset size increases since it checks each element one by one. Compared to the parallel version, the difference in speed becomes clearer with larger inputs, where dividing the task can reduce overall search time. This experience showed me that although sequential search is straightforward, it is not always the most efficient choice for large-scale problems.