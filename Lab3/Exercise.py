import time
import random
from math import sqrt

# 1. Modify linear search to return all indices where the target appears
def linear_search_all(arr, target):
    indices = [i for i, value in enumerate(arr) if value == target]
    return indices if indices else -1

# Test the modified linear search function
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search_all(test_list, 5)
print(f"Linear Search (all indices): Indices of 5 are {result}")

# 2. Binary search to find insertion point for a target in a sorted list
def binary_search_insertion_point(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left  # Position where target should be inserted

# Test the insertion point function
test_list_sorted = sorted(test_list)
target = 8
insertion_point = binary_search_insertion_point(test_list_sorted, target)
print(f"Insertion point for {target} is index {insertion_point}")

# 3. Count the number of comparisons in each search algorithm
def linear_search_count_comparisons(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons  # Return index and comparisons count
    return -1, comparisons

def binary_search_count_comparisons(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons

# Test the comparison count functions
linear_result, linear_comparisons = linear_search_count_comparisons(test_list, 6)
binary_result, binary_comparisons = binary_search_count_comparisons(test_list_sorted, 6)
print(f"Linear Search: Index of 6 is {linear_result}, Comparisons: {linear_comparisons}")
print(f"Binary Search: Index of 6 in sorted list is {binary_result}, Comparisons: {binary_comparisons}")

# 4. Implement jump search and compare with linear and binary search
def jump_search(arr, target):
    n = len(arr)
    step = int(sqrt(n))
    prev, comparisons = 0, 0

    # Finding the block where the target might be
    while arr[min(step, n) - 1] < target:
        comparisons += 1
        prev = step
        step += int(sqrt(n))
        if prev >= n:
            return -1, comparisons

    # Performing linear search within the block
    for i in range(prev, min(step, n)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

# Compare performance and comparison counts
def compare_search_algorithms(arr, target):
    # Linear Search
    start_time = time.time()
    linear_result, linear_comparisons = linear_search_count_comparisons(arr, target)
    linear_time = time.time() - start_time
    
    # Binary Search (on sorted array)
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result, binary_comparisons = binary_search_count_comparisons(arr_sorted, target)
    binary_time = time.time() - start_time

    # Jump Search (on sorted array)
    start_time = time.time()
    jump_result, jump_comparisons = jump_search(arr_sorted, target)
    jump_time = time.time() - start_time

    print(f"Linear Search: Found at index {linear_result}, Time: {linear_time:.6f} seconds, Comparisons: {linear_comparisons}")
    print(f"Binary Search: Found at index {binary_result}, Time: {binary_time:.6f} seconds, Comparisons: {binary_comparisons}")
    print(f"Jump Search: Found at index {jump_result}, Time: {jump_time:.6f} seconds, Comparisons: {jump_comparisons}")

# Test with a larger list
large_list = list(range(10000))
compare_search_algorithms(large_list, 8888)

# Recursive Binary Search remains unchanged
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Test the recursive function
result = binary_search_recursive(test_list_sorted, 6, 0, len(test_list_sorted) - 1)
print(f"Recursive Binary Search: Index of 6 in sorted list is {result}")