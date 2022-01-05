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



## leetcode problem: 4. Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 
# Constraints:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

def medianOfTwoSortedArray(nums1, nums2):
    # make the first array smaller
    if len(nums2) < len(nums1):
        return medianOfTwoSortedArray(nums2, nums1)

    m, n = len(nums1), len(nums2)    
    lo, hi = 0, m

    while lo <= hi:
        # total elements of left of nums1 and num2 should be equal to the total elemenet of right of nums1 and num2
        partX = (lo + hi) // 2
        partY = (m + n + 1) // 2 - partX

        # find the max left of partion and min right of partition
        maxLeftX = - 2**32 if partX == 0 else nums1[partX - 1]
        minRightX = 2**32 -1  if partX == m else nums1[partX]

        maxLeftY = - 2**32 if partY == 0 else nums2[partY - 1]
        minRightY = 2**32 -1  if partY == n else nums2[partY]

        # if the desired 4 nums are found
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            # if total number of elemeents is even
            if (m + n) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightY, minRightX) ) /2
            else:
                return max(maxLeftX, maxLeftY)   

        # maxLeftX is too big, decrease the hi; else increase the low
        elif maxLeftX > minRightY:
            hi = partX -1
        else:
            lo = partX + 1    

    # if not found
    return -2**32


# # --------------------------MAIN to TEST-------------------------------------
nums1 = [1,3]; nums2 = [2]
print(medianOfTwoSortedArray(nums1, nums2))

# # --------------------------MAIN to TEST-------------------------------------
nums1 = [100, 102, 103, 200, 400, 500, 504]; nums2 = [2]
print(medianOfTwoSortedArray(nums1, nums2))

