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


def twoSingleNumber(nums):
    # xor_sum will be xor of a and b where a and b are the target number
    xor_sum = 0
    for x in nums:
        xor_sum = xor_sum ^ x


    # now we need to seperate a and b from xor_sum
    # generate a number with one of the set_bits from xor_sum; 
    set_bit_num = xor_sum & (-xor_sum) # two's complement of xor

    # lets assume the set_bit comes from a; then the corresponding bit in b will be unset (0)
    # (a & set_bit_num) > 0 and (b & set_bit_num) == 0
    # devide the numbers on these condition; dont worry about repeating numbers, they will cancel each other; doesnot matter which group they belong

    sum1, sum2 = 0, 0

    for x in nums:
        if set_bit_num & x > 0:
            sum1 = sum1 ^ x
        else:
            sum2 = sum2 ^ x

    return [sum1, sum2]

# # --------------------------MAIN to TEST-------------------------------------
nums=[1,2,1,2,3,5,5,6,6,7]
print(twoSingleNumber(nums))
# # --------------------------MAIN to TEST-------------------------------------
nums=[1,10]
print(twoSingleNumber(nums))
