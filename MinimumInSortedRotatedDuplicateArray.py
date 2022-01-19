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

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()


def findMin(arr, low, high):
  
    while (low < high):
        mid = low + (high - low) // 2;

        print([arr[lo], arr[mid], arr[hi]])
        
        if (arr[mid] == arr[high]):
            high -= 1;
        elif (arr[mid] > arr[high]):
            low = mid + 1;
        else:
            high = mid;
    
    return arr[high];


# # --------------------------MAIN to TEST-------------------------------------
arr1 = [5, 6, 6, 1, 1, 2, 3, 4]; 
lo=0; hi=len(arr1)-1;
print(findMin(arr1, lo, hi))
# # --------------------------MAIN to TEST-------------------------------------
arr1 = [1,1, 2, 2, 3, 4];
lo=0; hi=len(arr1)-1;
print(findMin(arr1, lo, hi))# # --------------------------MAIN to TEST-------------------------------------
arr1 = [1];
lo=0; hi=len(arr1)-1;
print(findMin(arr1, lo, hi))
# # --------------------------MAIN to TEST-------------------------------------
arr1 = [1,1,1,2,2];
lo=0; hi=len(arr1)-1;
print(findMin(arr1, lo, hi))
# # # --------------------------MAIN to TEST-------------------------------------
# arr1 = [22, 22, 1, 1];
# lo=0; hi=len(arr1)-1;
# print(findMin(arr1, lo, hi))
# # # --------------------------MAIN to TEST-------------------------------------
# arr1 = [5, 5, 6, 6, 7, 7, 1,1, 1, 2,2,3, 3, 4];
# lo=0; hi=len(arr1)-1;
# print(findMin(arr1, lo, hi))
# # # --------------------------MAIN to TEST-------------------------------------
# arr1 = [1,1, 2,2,3, 3, 4, 5, 6, 7];
# lo=0; hi=len(arr1)-1;
# print(findMin(arr1, lo, hi))
# # # --------------------------MAIN to TEST-------------------------------------
