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
## leetcode problem: 617. Merge Two Binary Trees

# You are given two binary trees root1 and root2.

# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

# Return the merged tree.

# Note: The merging process must start from the root nodes of both trees.

# Example 1:
# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]

# Example 2:
# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]
 
# Constraints:
# The number of nodes in both trees is in the range [0, 2000].
# -104 <= Node.val <= 104

# # ---------------------------------------------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def mergeBinaryTrees(root1, root2):
    
    if root1 == None:
        return root2
    if root2 == None:
        return root1

    root1.val = root1.val + root2.val
    root1.left = mergeBinaryTrees(root1.left, root2.left)    
    root1.right = mergeBinaryTrees(root1.right, root2.right) 

    return root1   


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



# # --------------------------MAIN to TEST-------------------------------------
rootp=Node(1); 
rootp.left=Node(3); rootp.right=Node(2)
rootp.left.left = Node(5)

rootq=Node(2); 
rootq.left=Node(1); rootq.right=Node(3)
rootq.left.right=Node(4);
rootq.right.right=Node(7)

p_iot=inorder(rootp)
q_iot=inorder(rootq)

p_pot=inorder(rootp)
q_pot=inorder(rootq)

print(inorder(rootp))
print(inorder(rootq))

root_merged = mergeBinaryTrees(rootp, rootq)
print(inorder(root_merged))
