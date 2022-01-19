# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %  Solution Author: Rumana Aktar 
# %  Date: 01/05/2022
# %
# %  For more information, contact:
# %      Rumana Aktar
# %      226 Naka Hall (EBW)
# %      University of Missouri-Columbia
# %      Columbia, MO 65211
# %      rayy7@mail.missouri.edu
# # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



## leetcode problem: Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]

# # --------------------------Solution-------------------------------------
from SearchRotatedArray import findPivotIndex
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

def bSearch(nums, target, lo, hi):

    while lo <= hi:
        mid = (lo+hi) //2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return bSearch(nums, target, mid+1, hi)  
        else:
            return bSearch(nums, target, lo, mid-1)

    return  -1

def findFirst(nums, target, lo, hi):

    idx = -1

    while lo <= hi:

        mid = (lo + hi) // 2      
        
        if nums[mid] >= target:
            hi = mid -1
        else:
            lo = mid +1

        if nums[mid] == target:
            idx = mid 

    return idx            
            


def findLast(nums, target, lo, hi):

    idx = -1

    while lo <= hi:

        mid = (lo + hi) // 2      
        
        if nums[mid] <= target:
            lo = mid + 1
        else:
            hi = mid - 1

        if nums[mid] == target:
            idx = mid 
               
    return idx            
            


def findFirstLast(nums, target):

    leftIdx = findFirst(nums, target, 0, len(nums)-1)
    rightIdx = findLast(nums, target, 0, len(nums)-1) 

    return [leftIdx, rightIdx]   




# # --------------------------MAIN to TEST-------------------------------------
nums = [5,7,7,8,8,10]; target = 8
print(findFirstLast(nums, target))

# # --------------------------MAIN to TEST-------------------------------------
nums = [5,7,7,8,8,10]; target = 6
print(findFirstLast(nums, target))

nums = []; target = 0
print(findFirstLast(nums, target))
