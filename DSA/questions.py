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
