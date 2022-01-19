import os
from typing import ByteString; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

def findMountainPeak(nums, lo, hi):
    while lo < hi:
        
        
        mid = lo + (hi-lo) //2

        if mid > 0 and nums[mid-1] < nums [mid] and nums[mid] > nums[mid+1] and mid < len(nums)-1:
            return mid
        elif mid > 0 and nums[mid - 1] > nums[mid]:
            return findMountainPeak(nums, lo, mid-1)
        else:
            return findMountainPeak(nums, mid + 1, hi)
            
    return hi

def findPeakUtil(arr, low, high, n):
    
     # Find index of middle element
     # (low + high)/2 
    mid = low + (high - low)/2 
    mid = int(mid)
    
    # Compare middle element with its 
    # neighbours (if neighbours exist)
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) 
        and 
        (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return mid


    # If middle element is not peak and 
    # its left neighbour is greater 
    # than it, then left half must 
    # have a peak element
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return findPeakUtil(arr, low, (mid - 1), n)
    # its right neighbour is greater
    # than it, then right half must 
    # have a peak element
    else:
        return findPeakUtil(arr, (mid + 1), high, n)


# A wrapper over recursive 
# function findPeakUtil()
def findPeak(arr, n):

    return findPeakUtil(arr, 0, n - 1, n)


# # Driver code
# arr = [1, 3, 20, 4, 1, 0]
# n = len(arr)
# print("Index of a peak point is", findPeak(arr, n))
    
# # This code is contributed by 
# # Smitha Dinesh Semwal

nums=[3,9,8,6,4]
print(findMountainPeak(nums, 0, len(nums)-1))
