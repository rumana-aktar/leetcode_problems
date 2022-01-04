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

def preorder(root):
    if root==None:
        return

    st=[]
    st.append(root)
    pot=[]

    while len(st)>0:
        cur=st.pop()
        pot.append(cur.val)

        if root.right != None:
            st.append(root.right)
        elif root.left != None:
            st.append(root.left)

    return pot            

        



def sameTree(in1, in2, pre1, pre2):
    if len(in1) != len(in2) or len(pre1) != len(pre2) or len(in1)!=len(pre1):
        return False

    for i in range(len(in1)):
        if in1[i] != in2[i]:
            return False
    
    for i in range(len(pre1)):
        if pre1[i] != pre2[i]:
            return False

    return True

 


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

print(sameTree(p_iot, q_iot, p_pot, q_pot))


# # --------------------------MAIN to TEST-------------------------------------
# #p = [1,2,1], q = [1,1,2]
rootp=Node(1); rootp.left=Node(2); rootp.right=Node(1)
rootq=Node(1); rootq.left=Node(1); rootq.right=Node(2)

p_iot=inorder(rootp)
q_iot=inorder(rootq)

p_pot=inorder(rootp)
q_pot=inorder(rootq)

print(sameTree(p_iot, q_iot, p_pot, q_pot))


# # --------------------------MAIN to TEST-------------------------------------
# #p = [1,2,1], q = [1,1,2]
rootp=Node(1); rootp.left=Node(2); rootp.right=Node(1)
rootq=Node(1); rootq.left=Node(2); rootq.right=Node(1)

p_iot=inorder(rootp)
q_iot=inorder(rootq)

p_pot=inorder(rootp)
q_pot=inorder(rootq)

print(sameTree(p_iot, q_iot, p_pot, q_pot))
