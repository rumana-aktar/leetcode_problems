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

def containerWithMostWater(height):
    max_water, left, right = 0, 0, len(height)-1
        
    while left < right:
        max_water = max ( max_water, min (height[left], height[right]) * (right-left))
            
        if height[right] < height[left]:
            right -= 1
        else:
            left += 1
       
    return max_water


# # --------------------------MAIN to TEST-------------------------------------
height = [1,8,6,2,5,4,8,3,7]
print(containerWithMostWater(height))

# # --------------------------MAIN to TEST-------------------------------------
height = [1,1]
print(containerWithMostWater(height))

