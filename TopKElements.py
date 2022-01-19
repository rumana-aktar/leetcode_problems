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



## leetcode problem: 347. Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Constraints:
# 1 <= nums.length <= 105
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

import heapq

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

def topKFrequentElements(nums, k):
    
    res = []
    # calculate the frequencies
    d = {}
    for x in nums:
        if x in d:  d[x] += 1
        else:       d[x] = 1 

    # bucket sort according top values
    bckt = [[] for i in range(len(nums)+1)] 
    for key, val in d.items():
        bckt[val].append(key)

    # get the top k frequent elements
    i= len(bckt)-1
    while k > 0:
        for x in bckt[i]:
            res.append(x)
            k -= 1
        i -= 1    

    return res        



# # --------------------------MAIN to TEST-------------------------------------
nums = [6,7,6,6,7,7, 7, 6, 1,1,1,2,2,3]; k = 2
print(topKFrequentElements(nums, k))
# # --------------------------MAIN to TEST-------------------------------------
