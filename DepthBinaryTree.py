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
## leetcode problem: 104. Maximum Depth of Binary Tree

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2

# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100


# # ---------------------------------------------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# recursive 
def depthBinaryTree(root):
    if root == None:
        return 0
    return max( depthBinaryTree(root.left)+1, depthBinaryTree(root.right)+1)            


# # --------------------------MAIN to TEST-------------------------------------
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(depthBinaryTree(root))

# # --------------------------MAIN to TEST-------------------------------------
root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
root.right.right.right = Node(3)
print(depthBinaryTree(root))


# # --------------------------MAIN to TEST-------------------------------------
root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.right = Node(3)
root.right.right = Node(3)
print(depthBinaryTree(root))

# # --------------------------MAIN to TEST-------------------------------------
root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(2)
root.left.right = None
root.right.left = Node(2)
print(depthBinaryTree(root))

# # --------------------------MAIN to TEST-------------------------------------
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
print(depthBinaryTree(root))

# # --------------------------MAIN to TEST-------------------------------------
root = None
print(depthBinaryTree(root))