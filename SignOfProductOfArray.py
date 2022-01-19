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

def signFunc(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0

def signOfProductOfArray(nums):
    sign_prod = 1
    for x in  nums:
        sign_prod *= signFunc(x)
        if x == 0:
            return sign_prod

    return sign_prod        
        


# # --------------------------MAIN to TEST-------------------------------------

print(signOfProductOfArray([-1,-2,-3,-4,3,2,1]))

# # --------------------------MAIN to TEST-------------------------------------
print(signOfProductOfArray([1,5,0,2,-3]))

# # --------------------------MAIN to TEST-------------------------------------
print(signOfProductOfArray([-1,1,-1,1,-1]))
