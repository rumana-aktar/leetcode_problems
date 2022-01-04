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
## leetcode problem. 0977: Squares of a Sorted Array

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 
# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.


# # ---------------------------------------------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

def squaresSortedArray(nums):
    nums2=[]

    #create another array with negative numbers only
    i=0;
    while nums[i] < 0:
        nums2.append(nums[i])
        i+=1
    nums2.reverse()
    n=i
    m=len(nums)-n

    # square elements in nums and nums2
    while i<len(nums):
        nums[i] = nums[i]**2
        i+=1
    i=0
    while i < len(nums2):
        nums2[i]=nums2[i]**2 
        i+=1  


    
    #now sort
    i=n; j=0; k=0
    while i<m+n and j<n:
        if nums[i] <nums2[j]:
            nums[k] = nums[i]
            i+=1; k+=1
        else:
            nums[k]=nums2[j]
            k+=1; j+=1

    while i<m+n:
        nums[k]=nums[i]
        k+=1; i+=1

    while j<n:
        nums[k]=nums2[j]
        k+=1; j+=1      

    return nums         





def mergeTwoSortedLists(nums1, m, nums2, n):
    #copy the elements to the end of list1
    i=n-1; j=m+n-1
    while i>=0:
        nums1[j]=nums1[i]
        i-=1; j-=1

    #now sort
    i=n; j=0; k=0
    while i<m+n and j<n:
        if nums1[i] <nums2[j]:
            nums1[k] = nums1[i]
            i+=1; k+=1
        else:
            nums1[k]=nums2[j]
            k+=1; j+=1

    while i<m+n:
        nums1[k]=nums1[i]
        k+=1; i+=1

    while j<n:
        nums1[k]=nums2[j]
        k+=1; j+=1      

    return nums1          




# # --------------------------MAIN to TEST-------------------------------------
print(mergeTwoSortedLists([1,2,3,0,0,0], 3, [2,5,6], 3))
print(mergeTwoSortedLists([1], 1, [], 0))
print(mergeTwoSortedLists([0], 0, [1], 1))
print(squaresSortedArray([-4,-1,0,3,10]))
