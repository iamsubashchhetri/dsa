"""
Largest element in an array
nums=[55,32,-97,99,3,67]
"""

# def largest_num(nums):
#     largest = nums[0]
#     n = len(nums)
#     for i in range(0, n):
#         largest = max(largest, nums[i])
#     return largest


# print(largest_num([3,4,5,6,9,1]))

"""
Find the 2nd largest number"""


# sorted_array = sorted(nums)
# sendlargest = sorted_array[-2]
# print(f"second largest number:{sendlargest}")
# time complecity : o(n) and space complexity is O(1)

# Solution 2
# def second_largest(nums):
#     largest = float("-inf")
#     second_largest = float("-inf")
#     n = len(nums)
#     for i in range(0, n):
#         largest = max(largest,nums[i])
#     for i in range(0,n):
#         if nums[i]>second_largest and  nums[i] != largest:
#             second_largest =nums[i]

#     return second_largest

# print(second_largest(nums))

# optimal solution
# nums = [55, 32, 99, 54, 65, 64, 23, 100]
# largest = float("-inf")
# second = float("-inf")


# def secnd_largest(nums):
#     n = len(nums)
#     for i in range(0, n):
#         if nums[i] > largest:
#             secnd_largest = largest
#             largest = nums[i]
#         elif nums[i] > secnd_largest and nums[i] != largest:
#             secnd_largest = nums[i]

#     return secnd_largest


# # Time complexity is 0(N)
# # Space complexity is 0(1) because only 3 variable are used doesnt matter the length of array

""" Check if the array is osrted or not"""
nums = [3, 3, 5, 6, 7, 8]
# n = len(nums)


# def soretedornot(nums):
#     for i in range(0, n - 1):
#         if nums[i] > nums[i + 1]:
#             return False
#     return True


# print(soretedornot(nums))

"""Remove Duplicate from a sorted array"""
# NOt the proper way
# n = len(nums)


# def removed(nums):
#     for i in range(0, n - 2):
#         if nums[i] == nums[i + 1]:
#             nums.remove(nums[i + 1])

#     return nums


# print(removed(nums))

##OptimalSOlution
# nums = [1, 1, 1, 3, 3, 3, 3, 6, 6, 5, 6, 7, 8]


# def remove_duplicate(nums):
#     n = len(nums)
#     if n == 1:
#         return 1
#     i = 0
#     j = i + 1
#     while j < n:
#         if nums[j] != nums[i]:
#             i += 1
#             nums[i], nums[j] = nums[j], nums[i]
#         j += 1  # Always increment j
#     return i + 1
# print(remove_duplicate(nums))


# Right Rotate an Array by One Place

# nums = [1, 2, 3, 4, 5]
# n = len(nums)
# def rotate_array(nums):
#     last_element = nums[n-1]
#     for i in range(n-1,0,-1):
#         nums[i] = nums[i-1]
#     nums[0] = last_element
#     return nums


# print(rotate_array(nums))

# Time complexity is 0(N)
# Space complexity is 0(1)


# Left Rotate an Array by One Place
# nums = [1, 2, 3, 4, 5]



# def left_rotatae(nums):
#    left_element = nums[0]
#    n = len(nums)

#    for i in range(0, n - 1):
#         nums[i] = nums[i + 1]

#    nums[-1] = left_element

#    return nums


# print(left_rotatae(nums))


# RightRotate array by k Places
# from typing import List

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Rotates the array to the right by k steps in-place.
#         """
#         n = len(nums)
#         k = k % n  # Handle cases where k > n
#         nums[:] = nums[-k:] + nums[:-k]
#         # No return needed; modifies nums in-place

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # Handle cases where k > n

        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Step 1: Reverse last k elements
        reverse(n - k, n - 1)

        # Step 2: Reverse first n-k elements
        reverse(0, n - k - 1)

        # Step 3: Reverse whole array
        reverse(0, n - 1)

# Example usage:
# nums = [1,2,3,4,5,6,7]
# k = 3
# Solution().rotate(nums, k)
# print(nums)  # Output: [5,6,7,1,2,3,4]


