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



## leetcode problem: 
# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:
# Input: nums = [1], target = 0
# Output: -1
 

# Constraints:
# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104

# # --------------------------Solution-------------------------------------
import os
from typing import ByteString; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()


def findPivotIndex(nums):
    if len(nums) == 0:
        return -1

    if nums[0] < nums[len(nums)-1]:
        return 0

    lo, hi = 0, len(nums)-1

    while lo <= hi:
        mid = (lo + hi) // 2

        if mid < len(nums)-1 and nums[mid] > nums[mid + 1]:
            return mid + 1
            
        elif nums[0] <= nums[mid]:
            lo = mid + 1
        else:
            hi = mid - 1

    return nums[0]           

                

# def findPivotIndex(nums):
    
#     # empty array
#     if len(nums) == 0:
#         return -1

#     if nums[0] < nums[len(nums)-1]:
#         return 0

#     lo, hi = 0, len(nums)-1
#     while lo <= hi:
#         mid = (lo + hi) // 2

#         if mid < len(nums) and nums[mid] > nums[mid+1]:
#             return mid + 1
#         elif nums[lo] <= nums[mid]:
#             lo = mid + 1
#         else:
#             hi = mid -1

#     return 0                


    



def bSearch(nums, target, lo, hi):

    while lo <= hi:
        mid = (lo+hi) //2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return bSearch(nums, target, lo, mid-1)
        else:
            return bSearch(nums, target, mid+1, hi)  

    return -1        



def searchRotatedArray(nums, target):
    pivotIdx = findPivotIndex(nums)
    print("Pivot element: ", pivotIdx)

    if nums[pivotIdx] == target:
        return pivotIdx
    elif pivotIdx == 0:
        return bSearch(nums, target, 0, len(nums)-1)  
    elif target < nums[0]:
        return bSearch(nums, target, pivotIdx, len(nums)-1)
    else:
        return bSearch(nums, target, 0, pivotIdx-1)        

    




# # --------------------------MAIN to TEST-------------------------------------
# nums = [4,5,6,7,0,1,2]; target = 70
# print(searchRotatedArray(nums, target))

nums = [3,4,5,6,1,2]; target = 2
print(searchRotatedArray(nums, target))


# # --------------------------MAIN to TEST-------------------------------------

# %%
