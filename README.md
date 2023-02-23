# Python-Sorting-Algorithms

Summary of Sorting Algorithm Performance Experiment:

The experiment compares the performance of four different sorting algorithms: Selection Sort, Merge Sort, Bubble Sort, and Python Built-in Sort. The algorithms are tested on four different list sizes: 10, 100, 1000, and 10000. The experiment measures the execution time for each algorithm and list size combination and graphs the results.

Selection Sort works by iterating through the list and selecting the smallest element and swapping it with the first element. It then repeats this process for the remainder of the list. Selection Sort has a time complexity of O(n^2) in the worst case, where n is the number of elements in the list.

Merge Sort works by dividing the list into two halves, sorting each half recursively, and then merging the two halves together. Merge Sort has a time complexity of O(n log n) in the worst case.

Bubble Sort works by repeatedly swapping adjacent elements that are in the wrong order. It continues to iterate through the list until no more swaps are needed. Bubble Sort has a time complexity of O(n^2) in the worst case.

Python Built-in Sort uses the built-in sorting function in Python, which is a highly optimized implementation of the Timsort algorithm. Timsort has a time complexity of O(n log n) in the worst case.

The results of the experiment show that Python Built-in Sort is the fastest algorithm for all list sizes. Merge Sort is the second fastest, followed by Selection Sort and Bubble Sort. The difference in execution time between the fastest and slowest algorithms is most significant for larger list sizes. For example, for a list size of 10000, Python Built-in Sort is approximately 100 times faster than Bubble Sort.

In conclusion, the experiment demonstrates that the choice of sorting algorithm can have a significant impact on the execution time for large datasets. It is important to choose the appropriate algorithm for the specific problem and dataset to achieve optimal performance.
