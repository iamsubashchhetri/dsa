"""
Selection Sorting
nums=[5,7,8,4,1,6,9,2]
"""

# def selection_sorting(nums):
#     n = len(nums)
#     for i in range(0,n):
#         min_index = i
#         for j in range(i + 1, n):
#             if nums[j] < nums[min_index]:
#                 min_index = j
#         nums[i], nums[min_index] = nums[min_index], nums[i]  # Move inside the loop
#     return nums  # Add return statement

# print(selection_sorting([3, 4, 5, 2, 3, 5, 6, 3]))


"""Buble Sorting"""

# def buble_sorting(nums):

#     n= len(nums)

#     for i in range(n-2,-1,-1):
#         for j in range(0,i+1):
#          if nums[j]> nums[j+1]:
#           nums[j],nums[j+1]=nums[j+1],nums[j]
#     return nums

# print(buble_sorting([3,4,5,2,3,5,6,3]))

"""
    Insertion Sort"""

# n = len(nums)


# def insert_sort(nums):

#     for i in range(1, n):
#         key = nums[i]
#         j = i - 1
#         while j >= 0 and nums[j] > key:
#             nums[j + 1] = nums[j]
#             j=-1
#         nums[j+1]=key
#     return nums

'''Merge sorting in DSA
num= [3,4,5,2,3,5,6,3]

left=[3,4,5,2]  right =[3,5,6,3]'''

# def merge_array(left, right):
#     result = []
#     i, j = 0, 0
#     n, m = len(left), len(right)

#     while i < n and j < m:
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < n:
#         result.append(left[i])
#         i += 1

#     while j < m:
#         result.append(right[j])
#         j += 1

#     return result

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left_array = arr[:mid]
#     right_array = arr[mid:]

#     left = merge_sort(left_array)
#     right = merge_sort(right_array)

#     return merge_array(left, right)

# print("Merge Sort:", merge_sort([3, 4, 5, 2, 3, 5, 6, 3]))


'''
 Quick Sort algo
 nums=[4,1,7,6,3,2,8]
 1) Pick a pivot
 - it can be the fist element
 - it can be the last element
 - it can be the middle element
  - it can be any random element
  
  2) Put the Pivot at its correct Position/index'''

def partition(nums, low, high):
    pivot = nums[low]  # Use first element as pivot
    i = low + 1
    j = high
    while True:
        while i <= j and nums[i] <= pivot:
            i += 1
        while i <= j and nums[j] > pivot:
            j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            break
    nums[low], nums[j] = nums[j], nums[low]
    return j

def quicksort(nums, low, high):
    if low < high:
        p_index = partition(nums, low, high)
        quicksort(nums, low, p_index - 1)
        quicksort(nums, p_index + 1, high)

# Example usage:
nums = [4, 1, 7, 6, 3, 2, 8]
quicksort(nums, 0, len(nums) - 1)
print("Quick Sort (first element as pivot):", nums)


# Time Complexity (TC):
# Best Case:    O(n log n)   (pivot splits array evenly)
# Average Case: O(n log n)   (random input)
# Worst Case:   O(n^2)       (already sorted or reverse sorted, bad pivot choice)

# Space Complexity (SC):
# Best/Average: O(log n)     (recursion stack depth)
# Worst Case:   O(n)         (recursion stack depth for sorted input)













