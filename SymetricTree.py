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
## leetcode problem: 101. Symmetric Tree

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false
 
# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100


import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def isMirror(root1, root2):
    if root1 == None and root2 == None:
        return True

    if root1 != None and root2 !=None:
        if root2.val == root2.val:
            return isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)

    return False        



# # --------------------------MAIN to TEST-------------------------------------
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(isMirror(root, root))

# # --------------------------MAIN to TEST-------------------------------------
root = Node(1)

root.left = Node(2)
root.right = Node(2)

root.left.left = Node(3)
root.left.right = Node(4)

root.right.left = Node(4)
root.right.right = Node(3)

print(isMirror(root, root))

# # --------------------------MAIN to TEST-------------------------------------
root = Node(1)
root.left = Node(2)
root.right = Node(2)

root.left.right = Node(3)
root.right.right = Node(3)

root = Node(1)
root.left = Node(2)
root.right = Node(2)

root.left.left = Node(2)
root.left.right = None

root.right.left = Node(2)



print(isMirror(root, root))