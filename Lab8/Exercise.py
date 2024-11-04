def quick_sort_in_place(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_in_place(arr, low, pi - 1)
        quick_sort_in_place(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
quick_sort_in_place(test_arr, 0, len(test_arr) - 1)
print("In-Place Quick Sort Result:", test_arr)

def bubble_sort_early_stop(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort_early_stop(test_arr.copy())
print("Bubble Sort with Early Stop Result:", sorted_arr)

def merge_sort_hybrid(arr, threshold=10):
    if len(arr) <= threshold:
        return insertion_sort(arr)
    
    mid = len(arr) // 2
    left = merge_sort_hybrid(arr[:mid], threshold)
    right = merge_sort_hybrid(arr[mid:], threshold)
    
    return merge(left, right)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort_hybrid(test_arr)
print("Hybrid Merge Sort Result:", sorted_arr)

import matplotlib.pyplot as plt
import matplotlib.animation as animation

def bubble_sort_visual(arr):
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    ax.set_title("Bubble Sort Visualization")
    
    def update_fig(arr, rects):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
    
    def bubble_sort_gen(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    yield arr

    anim = animation.FuncAnimation(
        fig, func=update_fig, fargs=(bar_rects,), frames=bubble_sort_gen(arr), repeat=False, interval=50
    )
    plt.show()

# Test the visualization
test_arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort_visual(test_arr.copy())