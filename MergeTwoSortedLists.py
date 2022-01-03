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
## leetcode problem 


# # ---------------------------------------------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

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
