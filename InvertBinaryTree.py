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
## leetcode problem 226. Invert Binary Tree

# Given the root of a binary tree, invert the tree, and return its root.

# Example 1:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Example 2:
# Input: root = [2,1,3]
# Output: [2,3,1]

# Example 3:
# Input: root = []
# Output: []
 
# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder(root):
    if root == None:
        return
    st=[]
    cur=root
    iot=[]

    while True:
        if cur != None:
            st.append(cur)
            cur=cur.left
        elif st:
            cur=st.pop()
            iot.append(cur.val)
            cur=cur.right
        else:
            break
    return iot


def invertBinaryTree(root):

    if root :
        temp = root.left
        root.left = invertBinaryTree(root.right)
        root.right = invertBinaryTree(temp)
        
    return root
    



# # --------------------------MAIN to TEST-------------------------------------
root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(9)
#----print original binary tree inorder
iot=inorder(root)    
print(iot)  
#----print INVERTED binary tree inorder
rootp = invertBinaryTree(root)
pot=inorder(rootp)
print(pot)


# # --------------------------MAIN to TEST-------------------------------------
root = Node(2)
root.left = Node(1)
root.right = Node(3)
#----print original binary tree inorder
iot=inorder(root)    
print(iot)  
#----print INVERTED binary tree inorder
rootp = invertBinaryTree(root)
pot=inorder(rootp)
print(pot)
