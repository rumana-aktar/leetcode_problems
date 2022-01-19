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

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.

# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length


# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()
from collections import deque

def slidingWindowMaximum(nums, k):

    res = []
    q = deque()
    l, r = 0, 0

    while r < len(nums):

        # check if queue elements are smaller , then pop
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        # take care of out of window elements from left
        if l > q[0]:
            q.popleft()

        # get the maximum when the window hits k elements
        if r + 1 >= k:
            res.append(nums[q[0]])
            l += 1

        r += 1   

    return res     


    





# # --------------------------MAIN to TEST-------------------------------------
nums = [1,3,-1,-3,5,3,6,7]; k = 3
print(slidingWindowMaximum(nums, k))

# # --------------------------MAIN to TEST-------------------------------------
nums = [1]; k = 1
print(slidingWindowMaximum(nums, k))
