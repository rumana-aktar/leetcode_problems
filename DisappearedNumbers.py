# # ---------------------------------------------------------------------------
#   Solution Author: Rumana Aktar 
#   Date: 12/28/2021
# 
#   For more information, contact:
#       Rumana Aktar
#       226 Naka Hall (EBW)
#       University of Missouri-Columbia
#       Columbia, MO 65211
#       rayy7@mail.missouri.edu
# # ---------------------------------------------------------------------------

# # ---------------------------------------------------------------------------
## leetcode problem: 448. Find All Numbers Disappeared in an Array

# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Example 2:
# Input: nums = [1,1]
# Output: [2]

# Constraints:
# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n

# # ---------------------------------------------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()


def disappearedNumbers(nums):
    
    # for x in nums, mark nums[x-1] as negative
    for i in range(len(nums)):
        x=abs(nums[i])
        nums[x-1] = - abs(nums[x-1])

    # return all numbers which are unmarked or positive
    dis_nums=[]
    for i in range(len(nums)):
        if nums[i] > 0:
            dis_nums.append(i+1)
    return dis_nums        

    

# # --------------------------MAIN to TEST-------------------------------------
print(disappearedNumbers([4,3,2,7,8,2,3,1]))
print(disappearedNumbers([1,1]))