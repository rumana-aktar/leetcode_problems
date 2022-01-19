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

def oneSingleRestTrice(nums):

    # for handling negative numbers
    count_negs = 0
    for x in nums:
        if x < 0:
            count_negs += 1
   

    tn, tnp1, tnp2 = 2**32-1, 0, 0

    for x in nums:
        ctn, ctnp1, ctnp2 = tn & x, tnp1 & x, tnp2 & x

        # set and unset according to ctn
        tn = tn & (~ctn)
        tnp1 = tnp1 | ctn

        # set and unset according to ctnp1
        tnp1 = tnp1 & (~ctnp1)
        tnp2 = tnp2 | ctnp1

        # set and unset according to ctn
        tnp2 = tnp2 & (~ctnp2)
        tn = tn | ctnp2

    # if count_negs is multiple of negative, then target number is positive
    # else, target number must bee negative
    if count_negs % 3 == 0:
        return tnp1
    else:
        return -tnp1




# # --------------------------MAIN to TEST-------------------------------------
nums = [2,2,3,2]
print(oneSingleRestTrice(nums))
# # --------------------------MAIN to TEST-------------------------------------
nums = [0,1,0,1,0,1,99]
print(oneSingleRestTrice(nums))
