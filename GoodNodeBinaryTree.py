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


# # ---------------------------------------------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# recursive 

def dfs(root, max):

    if root == None:
        return 0
    
    if root.val >= max:
        max = root.val
        return 1 + dfs(root.left, max) + dfs(root.right, max)
    else:
        return dfs(root.left, max) + dfs(root.right, max)    





def goodNodeBinaryTree(root):
    if root == None:
        return 0
    return dfs(root, -2**32)    
    
      






# # --------------------------MAIN to TEST-------------------------------------
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(goodNodeBinaryTree(root))

# # --------------------------MAIN to TEST-------------------------------------
root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
root.right.right.right = Node(3)


# # --------------------------MAIN to TEST-------------------------------------
root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.right = Node(3)
root.right.right = Node(3)

# # --------------------------MAIN to TEST-------------------------------------
root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(2)
root.left.right = None
root.right.left = Node(2)

# # --------------------------MAIN to TEST-------------------------------------
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)

# # --------------------------MAIN to TEST-------------------------------------
root = None
