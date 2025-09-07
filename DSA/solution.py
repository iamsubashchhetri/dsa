'''
Time and Space Complexity
Rate of increase in timw woth respect to input size is TS

Exmaple 1

for  i in range(1, n+1):
for j in range(1,n+1):


O(n2)


for i in ranfe(1,n+1):
 for j in range(1,i+1)

 i  j
 1   1
 2   2
 3   3
 N   N
 N(N+1)/2
 = n2/2 + n/2
 =1/2n2
 =n2
 O(n2)

 
 Space Complexity
 = Memory space
 Axuillary space = extra space used to solve the problem

 input space = the space used to store the input   

'''

''''
Count the Number of Digits in an Integer
'''
# n= 5438
# num =n
# count=0
# while num>0:
#     count +=1
#     num =num//10
# print(count)

# from math import *
# def countDigit(num):
#     return int(log10(num)+1)

# print(countDigit(5438))
# Time complexity= O(log10(N))
#Space complexity = O(1)

'''
Check Palindrome'''
# def isPalindrome(n):
#    num = n
#    result=0
#    while num>0:
#     ld = num%10
#     result = (result*10)+ld
#     num = num//10
#     return n==result
# print(isPalindrome(1234))
# print(isPalindrome(1221))

''' Armstrong Number  ie 153'''
# def armString(n):
#     nod= len(str(n))
#     num=n
#     total =0
#     while num >0:
#         ld = num%10
#         total += ld**nod
#         num =num//10
#     return total
# print(armString(153))

'''
Print All Factors of a Given Number
10=> 1,2,5,10'''


# def factor(num):
#    result =[]
#    for i in range(1,num+1):
#       if num%i == 0:
#          result.append(i)
#    return result
# print(factor(20))
#TC=> O(N/2) => O(N)
      
# Space complexity = O(k) k would be total number of factors
 #BEtter Solution
# def factor(num):
#    result =[]
#    for i in range(1,num//2+1):
#       if num%i == 0:
#          result.append(i)
#    result.append(num)
#    return result
# print(factor(20))
      
#OPtimumm Solution
# from math import sqrt
# def factor(num):
#     result =[]
#     for i in range(1, int(sqrt(num)+1)):
#         if  num%i == 0:
#             result.append(i)
#             if i != num // i:
#                 result.append(num // i)
#     result.sort()
#     return result

# print(factor(36 ))

'''Store Frequency in Dictionary
example dict =[2,3,3,3,5,5,6,6,2,2]
'''

# def fremap(nums):
#     frequency_map = dict()
#     for i in range(0, len(nums)):
#         if nums[i] in frequency_map:
#             frequency_map[nums[i]] += 1
#         else:
#             frequency_map[nums[i]] = 1
#     return frequency_map

# print(fremap([3,3,3,3,4,4,4,4,5,6,6,6,6,7,7,7]))


## Using hash map


# def hash_map(nums):
#   hash = {}
#   n = len(nums)
#   for i in range(0, n):
#     hash[nums[i]] = hash.get(nums[i], 0) + 1
#   return hash
# print(hash_map([3,3,3,3,4,4,4,4,5,6,6,6,6,7,7,7]))


### HASHING IN PYTHON 

# n=[5,3,2,2,2,1,5,5,7,5,10]
# m=[10,11,1,9,5,67,2]

# hash_list =[0]*11

# for num in n:
#      hash_list[num]+=1
     
# for num in m:
#     if num<1 or num>10:
#         print(0)
# else:
#     print(hash_list[num]) 
     
# n = [5, 3, 2, 2, 2, 1, 5, 5, 7, 5, 10]
# m = [10, 11, 1, 9, 5, 67, 2]
# def hashing(nums,queries):
#     freq ={}
#     for i  in range(len(nums)):
#         freq[nums[i]] = freq.get(nums[i], 0) + 1

#     for q in queries:
#         print(f"{q} → {freq.get(q, 0)}")
        
# hashing(n,m)

# chars = list("programming")       # first list of characters
# queries = ['g', 'm', 'z', 'r', 'o']   # second list (queries)

# def char_hashing(chars,queries):
#      freq={}
     
#      for chr in chars:
#          freq[chr] = freq.get(chr,0)+1
#      for q in queries:
#          print(f"{q}-> {freq.get(q,0)}")

# char_hashing(chars,queries)
    
'''
Recursion'''

# def fibonacci(n):
#     if n == 0:  # base case
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)  # recursive case

# print(fibonacci(2))  # Output: 13

'''
Reverse an array using resucriosn
array=[1,2,3,4,5]'''
# array=[1,2,3,4,5]
# def reverFnc(array,left,right):
#     if left >= right:
#         return
       
#     array[left], array[right] = array[right], array[left]
#     return reverFnc(array,left+1,right-1)

# reverFnc(array,0,len(array)-1)
# print(array)

'''
Palindrome or not using recursion'''

# ...existing code...

# name = ["n", "i", "t", "i", "n"]

# def palin(name, left, right):
#     if left >= right:
#         print("Number is palindrome")
#         return True
#     if name[left] != name[right]:
#         print("Number is not palindrome")
#         return False
#     return palin(name, left + 1, right - 1)

# palin(name, 0, len(name) - 1)

# # ...existing code...

''' Fibonacci number-
number=[0,1,1,2,3,5,8,13,21,34]'''

# class Solution:
#     def func(self,num):
#         if num==0 or num==1:
#             return num
#         return self.func(num-1)+self.func(num-2)
    
#     def fib(self,n:int)-> int:
#         return self.func(n)
        
# sol = Solution()
# print(sol.fib(6))
