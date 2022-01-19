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
## leetcode problem 


# # ---------------------------------------------------------------------------

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




def closestValue(root, target):
    res = root.val
    while root:
        if abs(root.val - target) < abs(res-target):
            res = root.val
        root = root.left if root.val > target else root.right

    return res      


 


# # --------------------------MAIN to TEST-------------------------------------
#p = [1,2,3], q = [1,2,3]
rootp=Node(1); rootp.left=Node(2); rootp.right=Node(3)
rootq=Node(1); rootq.left=Node(2); rootq.right=Node(3)

#p = [1,2], q = [1,null,2]
rootp=Node(1); rootp.left=Node(2)
rootq=Node(1); rootq.left=None; rootq.right=Node(2)

p_iot=inorder(rootp)
q_iot=inorder(rootq)

p_pot=inorder(rootp)
q_pot=inorder(rootq)

print(closestValue(rootp, 4))


# # --------------------------MAIN to TEST-------------------------------------
# #p = [1,2,1], q = [1,1,2]
rootp=Node(1); rootp.left=Node(2); rootp.right=Node(1)
rootq=Node(1); rootq.left=Node(1); rootq.right=Node(2)

p_iot=inorder(rootp)
q_iot=inorder(rootq)

p_pot=inorder(rootp)
q_pot=inorder(rootq)



# # --------------------------MAIN to TEST-------------------------------------
# #p = [1,2,1], q = [1,1,2]
rootp=Node(1); rootp.left=Node(2); rootp.right=Node(1)
rootq=Node(1); rootq.left=Node(2); rootq.right=Node(1)

p_iot=inorder(rootp)
q_iot=inorder(rootq)

p_pot=inorder(rootp)
q_pot=inorder(rootq)

