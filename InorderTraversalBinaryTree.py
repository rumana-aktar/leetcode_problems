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
## leetcode problem: 0094. Binary Tree Inorder Traversal

# Given the root of a binary tree, return the inorder traversal of its nodes' values.


# # ---------------------------------------------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printInorder(root):
    st=[]
    cur=root

    while True:
        if cur != None:
            st.append(cur)
            cur=cur.left
        elif st:
            cur=st.pop()
            print(cur.val, end=" ")
            cur=cur.right    
        else:
            break


    

# # --------------------------MAIN to TEST-------------------------------------
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(50)

print("Preorder traversal of binary tree is: ", end="")
printInorder(root)

root = Node(1)
root.left = Node(2)

print("\nPreorder traversal of binary tree is: ", end="")
printInorder(root)