# #Binary Search
# #Iterative Solution
# # nums=[2,46,7,9,11,18,19]

# def binarySearch(nums,target):
#     n=len(nums)
#     low=0
#     high=n-1
#     while low<=high:
#         mid=(low+high)//2
#         if nums[mid]==target:
#             return mid
#         elif nums[mid]<target:
#             low=mid+1
        
#         else:
#             high=mid-1
#     else:
#         high = mid-1
#     return -1

# #TIme Complexity-> log2(N)
# #Space Complexity-> 0(1)

#  ########Recurcive BInary search

# def binarySearch(nums, low, high, target):
#     if low > high:
#         return -1
#     mid = (low + high) // 2
#     if nums[mid] == target:
#         return mid
#     elif nums[mid] < target:
#         return binarySearch(nums, mid+1, high, target)
#     else:
#         return binarySearch(nums, low, mid-1, target)

# #Lower Bound
# # nums=[1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]

# def loweBound(nums):
     
#  n=len(nums)
#  target=7
#  lb=-1
#  low=0,high=n-1
#  while low<=high:
#     mid=(low+high)//2
#     if nums[mid]>=target:
#         lb=mid
#         high=mid-1
#     else:
#         low=mid+1
#  return lb

# ##########Upper bound
# # nums=[1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]

# def upperBound(nums):
#     n= len(nums)
#     target=7
#     ub=n
#     low=0,high = n-1
#     while low<=high:
#         mid=(low+high)//2
#         if nums[mid]>target:
#             ub=mid
#             high =mid-1
#         else:
#             low=mid+1
#     return ub
            
# ##########################################
# # Leetcode 35: Search Insert Position
# ##########################################
# from typing import List

# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         """
#         Find the index at which target should be inserted in sorted array nums.
#         If target exists, return its index. Otherwise return the index where
#         it would be if it were inserted in order.

#         Example:
#         nums = [1,3,5,6], target = 5 → return 2
#         nums = [1,3,5,6], target = 2 → return 1
#         nums = [1,3,5,6], target = 7 → return 4

#         Approach:
#         - Binary search to find the "lower bound"
#         - 'lb' stores the candidate index
#         - If nums[mid] >= target, move left
#         - Else, move right
#         """
#         n = len(nums)
#         lb = n                # default if target > all elements
#         low, high = 0, n - 1

#         while low <= high:
#             mid = (low + high) // 2

#             if nums[mid] >= target:
#                 lb = mid      # candidate index for target
#                 high = mid - 1
#             else:
#                 low = mid + 1

#         return lb


# ##########################################
# # Floor & Ceil Problem using Binary Search
# ##########################################
# def floor_ceil(nums, target):
#     """
#     Given a sorted array nums and a target value,
#     return the floor and ceil of the target.

#     Floor: greatest element <= target
#     Ceil:  smallest element >= target

#     Example:
#     nums = [2, 4, 6, 8, 10], target = 7
#     → floor = 6, ceil = 8
#     """
#     # n = len(nums)
#     # low, high = 0, n - 1
#     # floor_val, ceil_val = -1, -1   # -1 if no valid floor/ceil found

#     # while low <= high:
#     #     mid = (low + high) // 2

#     #     if nums[mid] == target:
#     #         return nums[mid], nums[mid]   # both floor & ceil are target itself

#     #     elif nums[mid] < target:
#     #         floor_val = nums[mid]         # candidate floor
#     #         low = mid + 1                 # move right to find larger values

#     #     else:  # nums[mid] > target
#     #         ceil_val = nums[mid]          # candidate ceil
#     #         high = mid - 1                # move left to find smaller values

#     # return floor_val, ceil_val


# ##########################################
# # Time & Space Complexity
# ##########################################
# # Search Insert Position → O(log N) time, O(1) space
# # Floor & Ceil Problem   → O(log N) time, O(1) space


##    Find the first and last occurance of target value
from typing import List

class Solution:
    def first(self, nums, target):
        n = len(nums)
        lb = -1
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                lb = mid
                high = mid - 1   # search left for earlier index
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return lb

    def last(self, nums, target):
        n = len(nums)
        hb = -1
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                hb = mid
                low = mid + 1    # search right for later index
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return hb

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.first(nums, target)
        hb = self.last(nums, target)
        return [lb, hb]
#Time complexity -> O(2log(N)) ie O(logN)
#Space complexity  -> O(1)

"""
Given a sorted array nums and a target, find how many times the target appears.

Example:

nums = [1,1,1,2,2,2,2,2,3,4,5]
target = 2
# Output: 3

"""
#Bruteforce Solution
nums = [1,2,2,2,2,3,4,5]
def find_occurance(nums):
    count=0
    n=len(nums)
    for i in range(n):
        if nums[i]==2:
            count+=1
        
    return count

print(find_occurance(nums))

#Optimal Solution

from typing import List

class Solution:
    def first(self, nums, target):
        lb = -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                lb = mid
                high = mid - 1   # search left
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return lb

    def last(self, nums, target):
        hb = -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                hb = mid
                low = mid + 1    # search right
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return hb

    def countOccurrences(self, nums: List[int], target: int) -> int:
        lb = self.first(nums, target)
        if lb == -1:
            return 0  # target not found
        hb = self.last(nums, target)
        return hb - lb + 1
nums = [1,1,1,2,2,2,2,2,3,4,5]
target = 2
sol = Solution()
print(sol.countOccurrences(nums, target))


             
"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""
class Solution:

    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low=0
        high=n-1
      
        while low<=high:
            mid=(high+low)//2
            if nums[mid] == target:
                return mid
            if nums[mid]<= nums[high]:
                if nums[mid]<=target<=nums[high]:
                    low=mid+1
                
                else:
                    high=mid-1
            else:
                if nums[low]<=target<=nums[mid]:
                    high = mid-1
                else:
                 low= mid+1
        return -1

#Search in Rotated Sorted Array II
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True

            # If we cannot decide (duplicates)
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

            # Right half sorted
            if nums[mid] <= nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

            # Left half sorted
            else:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

        return False

#Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        mini=float("inf")
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]<=nums[high]:
                mini=min(mini,nums[mid])
                high=mid-1
            else:
                mini=min(mini,nums[low])
                low =mid+1

        return mini

            


