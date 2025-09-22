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

# from typing import List


# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         n = len(nums)
#         k = k % n  # Handle cases where k > n

#         def reverse(left: int, right: int) -> None:
#             while left < right:
#                 nums[left], nums[right] = nums[right], nums[left]
#                 left += 1
#                 right -= 1

#         # Step 1: Reverse last k elements
#         reverse(n - k, n - 1)

#         # Step 2: Reverse first n-k elements
#         reverse(0, n - k - 1)

#         # Step 3: Reverse whole array
#         reverse(0, n - 1)


# Example usage:
# nums = [1,2,3,4,5,6,7]
# k = 3
# Solution().rotate(nums, k)
# print(nums)  # Output: [5,6,7,1,2,3,4]


# LINEAR SEARCH

# nums=[5,3,9,8,1,6,4,-10,-100] target=4
# nums = [5, 3, 9, 8, 1, 6, 4, -10, -100]


# def linear_search(nums):
#     n = len(nums)
#     for i in range(0, n):
#         if nums[i] == 4:
#             return i
#     return -1


# print(linear_search(nums))
# # Time COmplexity= O(N)
# # SC= O(1)

# # Merge 2 Sorted Arrays Without Duplicates
# nums1 = [1, 1, 1, 2, 4, 6, 7]
# nums2 = [1, 2, 3, 6, 7, 8, 9, 10]

# def sorted_array(nums1, nums2):
#     n, m = len(nums1), len(nums2)
#     result = []
#     i = j = 0

#     while i < n and j < m:
#         if nums1[i] <= nums2[j]:
#             if len(result) == 0 or result[-1] != nums1[i]:
#                 result.append(nums1[i])
#             i += 1
#         else:
#             if len(result) == 0 or result[-1] != nums2[j]:
#                 result.append(nums2[j])
#             j += 1

#     while i < n:
#         if len(result) == 0 or result[-1] != nums1[i]:
#             result.append(nums1[i])
#         i += 1

#     while j < m:
#         if len(result) == 0 or result[-1] != nums2[j]:
#             result.append(nums2[j])
#         j += 1

#     return result

# print(sorted_array(nums1, nums2))
# # Time = O(n + m)
# # Space = O(n + m) (for the result array).If we don’t count the output list the extra space used is just O(1).

# # You are given an array of size n containing distinct numbers from 0 to n.
# # That means the array has n numbers but one number is missing.
# # You need to find the missing number.

# # OPTIMAL
# def missingNumber(nums):
#     n = len(nums)
#     total = n * (n + 1) // 2
#     return total - sum(nums)


# print(missingNumber([3,0,1]))  # Output: 2
# # Time: O(n)
# # Space: O(1)

# # NOT OPTIMAL
# def missingNumber(nums):
#     nums.sort()
#     for i in range(len(nums)):
#         if nums[i] != i:
#             return i
#     return len(nums)
# ==========================
# Two Sum Problem - Brute Force
# ==========================
nums = [5, 9, 1, 2, 4, 15, 6, 3]  # target=13
target = 13


def two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):  # j goes from i+1 to end
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


# print(two_sum(nums, target))


# ==========================
# Two Sum Problem - Optimal Solution
# ==========================
def sum_two(nums, target):
    n = len(nums)
    hash_map = {}

    for i in range(n):  # loop over all indexes
        remaining = target - nums[i]
        if remaining in hash_map:
            return [hash_map[remaining], i]
        hash_map[nums[i]] = i

    return None  # if no pair found


print(sum_two(nums, target))


# ==========================
# Maximum Subarray Sum - Brute Force
# ==========================
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def max_subarray(nums):
    n = len(nums)
    total = 0
    maxi = float("-inf")

    for i in range(0, n):
        for j in range(i, n):
            total = total + nums[j]
            maxi = max(maxi, total)
    return maxi


# ==========================
# Maximum Subarray Sum - Optimal Solution (Kadane's Algorithm)
# ==========================
def maxi_sum(nums):
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    n = len(nums)
    maxi = float("-inf")
    total = 0
    for i in range(0, n):
        total = total + nums[i]
        maxi = max(maxi, total)
        if total < 0:
            total = 0
    return maxi


print(maxi_sum(nums))
# TC-> 0(N)
# SC -> 0(1)


# ==========================
# Best Time to Buy and Sell Stock (LeetCode 121)
# # ==========================
# def best_time(prices):
#     min_price = float("inf")
#     max_profit = 0
#     n = len(prices)

#     for i in range(n):
#         min_price = min(min_price, prices[i])
#         max_profit = max(max_profit, prices[i] - min_price)

#     return max_profit


# prices = [7, 2, 1, 5, 6, 4, 8]
# print(best_time(prices))  # Output: 7 (buy at 1, sell at 8)
# TC->  0(N)
# SC -> o(1) because  3 variable used but fixed size of variable regardless of length


# ==========================
# Rearrange Array Elements by Sign (LeetCode 2149)
# ==========================
# nums = [3, 1, -2, -5, 2, -4]


# def rearrange(nums):
#     n = len(nums)
#     pos, neg = 0, 1
#     result = [0] * n

#     for i in range(0, n):
#         if nums[i] >= 0:
#             result[pos] = nums[i]
#             pos += 2
#         else:
#             result[neg] = nums[i]
#             neg += 2

#     return result


# Time Complexity -> 0(N)
# Space Complexity -> 0(N)


#Leetcode 128: Longest Consecutive Sequence
 #Bruteforce Solution
nums=[1,99,101,98,2,5,3,100,1,1]

def consecutive(nums):
    n=len(nums)
    for i in range(0,n):
        max_count=1
        num=nums[i]
        while num+1 in nums:
            count +=1
            num=num+1
        max-count= max(max_count,count)
    return max_count

#TC-> O(N^2)
#SC-> O(1)
#Beter Solution
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        last_smaller=float("-inf")
        longest=0
        n=len(nums)
        for i in range(0,n):
            num=nums[i]
            if num-1==last_smaller:
             count+=1
             last_smaller=num
            elif num!=last_smaller:
                count=1
                last_smaller=num
            longest=max(longest,count)
        return longest

#Optimal Solution leetcode 128

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        my_set = set(nums)
        longest = 0

        for num in my_set:
            if num - 1 not in my_set:  # only start from sequence beginning
                x = num
                count = 1
                while x + 1 in my_set:
                    count += 1
                    x += 1
                longest = max(longest, count)

        return longest
# Time Complexity: O(n)

# Space Complexity: O(n)