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



## leetcode problem: 35. Search Insert Position

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4
 
# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

def searchInsertPosition(nums, target):


    if len(nums) ==0 or target < nums[0]:
        return 0
    if nums[len(nums)-1] > target:
        return len(nums)   
    
    lo, hi = 0, len(nums)-1

    while lo <= hi:
        mid = (lo + hi) //2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi =  mid -1    

    return lo




# # --------------------------MAIN to TEST-------------------------------------
nums = [1,3]; target = 2
print(searchInsertPosition(nums, target))

# # --------------------------MAIN to TEST-------------------------------------
nums = [1,3,5,6]; target = 2
print(searchInsertPosition(nums, target))

# # --------------------------MAIN to TEST-------------------------------------
nums = [1,3,5,6]; target = 7
print(searchInsertPosition(nums, target))

# # --------------------------MAIN to TEST-------------------------------------
nums = [1,3,5,6]; target = 0
print(searchInsertPosition(nums, target))

# # --------------------------MAIN to TEST-------------------------------------
nums = []; target = 7
print(searchInsertPosition(nums, target))


