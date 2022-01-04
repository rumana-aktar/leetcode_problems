# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %  Solution Author: Rumana Aktar 
# %  Date: 12/28/2021
# %
# %  For more information, contact:
# %      Rumana Aktar
# %      226 Naka Hall (EBW)
# %      University of Missouri-Columbia
# %      Columbia, MO 65211
# %      rayy7@mail.missouri.edu
# # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



## leetcode problem: 67 (https://leetcode.com/problems/add-binary/)

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]



import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()


def addBinaryString(a, b):
    res=""

    i=len(a)-1; j=len(b)-1; carry=0
    while i >=0 or j >=0:

        #get the sum
        if i>=0 and j >=0:
            sum=ord(a[i])+ord(b[j])-ord('0')-ord('0')+carry
            i-=1; j-=1
        elif i>=0:
            sum=ord(a[i])-ord('0')+carry
            i-=1
        elif j>=0:
            sum=ord(b[j])-ord('0')+carry
            j-=1

        #calculate the carry
        if sum == 3:
            res='1'+res
            carry=1
        elif sum == 2:
            res='0'+res
            carry=1
        elif sum == 1:
            res='1'+res
            carry=0    
        else:
            res='0'+res
            carry=0
    if carry:
        res='1'+res        

    return res

print(addBinaryString("1", "111"))




