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



## leetcode problem: 215
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
 
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 
# Constraints:
# 1 <= k <= nums.length <= 104
# -104 <= nums[i] <= 104

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

def kthLargest(nums, k):
    k=len(nums)-k

    def quickSelect(l, r):
        pivot, sidx = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[sidx], nums[i] = nums[i], nums[sidx]
                sidx += 1
        nums[r], nums[sidx] = nums[sidx], nums[r]   

        if k == sidx:
            return pivot
        elif sidx < k:
            return quickSelect(sidx+1, r)
        else:
            return quickSelect(l, sidx-1)            

    return quickSelect(0, len(nums)-1)




# # --------------------------MAIN to TEST-------------------------------------
nums = [3,2,1,5,6,4]; k = 6
print(kthLargest(nums, k))
# # --------------------------MAIN to TEST-------------------------------------
nums = [3,2,3,1,2,4,5,5,6]; k = 4
print(kthLargest(nums, k))