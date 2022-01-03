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
## leetcode problem: 160. Intersection of Two Linked Lists

# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
# For example, the following two linked lists begin to intersect at node c1:
# The test cases are generated such that there are no cycles anywhere in the entire linked structure.

# Note that the linked lists must retain their original structure after the function returns.
# Custom Judge:

# The inputs to the judge are given as follows (your program is not given these inputs):

# intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
# listA - The first linked list.
# listB - The second linked list.
# skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
# skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
# The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

 
# Example 1:
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: Intersected at '8'
# Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
# From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

# Example 2:
# Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# Output: Intersected at '2'
# Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
# From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

# Example 3:
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: No intersection
# Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.\ 


# Constraints:
# The number of nodes of listA is in the m.
# The number of nodes of listB is in the n.
# 1 <= m, n <= 3 * 104
# 1 <= Node.val <= 105
# 0 <= skipA < m
# 0 <= skipB < n
# intersectVal is 0 if listA and listB do not intersect.
# intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.


# # ---------------------------------------------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
 
    # Method to display the list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("")    

    def push(self, val):
        node = Node(val)
        if self.head == None:
            self.head=node
            return
        
        cur=self.head
        while cur.next:
            cur=cur.next
        cur.next=node

    def findIntersection(self, head2):
        head1 = self.head
        if head1 == None:
            return None
        if head2 == None:
            return None    

        #get the headcounts
        l1, l2 = 0, 0
        cur1, cur2 = head1, head2

        while cur1:
            l1 += 1
            cur1 = cur1.next
        while cur2:
            l2 += 1
            cur2 =cur2.next

        #get the differencee
        diff = l1 - l2
        cur1, cur2 = head1, head2
        
        if diff > 0:
            while diff:
                cur1 = cur1.next
                diff -= 1
        else:
            diff = - diff
            while diff:
                cur2 = cur2.next
                diff -= 1

        #iterate until common node is found
        while cur1 != cur2:
            cur1, cur2 = cur1.next, cur2.next               

        return cur1


# # --------------------------MAIN to TEST-------------------------------------
list1 = LinkedList();
list1.push(100);list1.push(200); list1.push(300);list1.push(11); list1.push(12); list1.push(13); list1.push(14);
list1.printList()

list2 = LinkedList();
list2.push(1);list2.push(2); list2.head.next.next = list1.head.next.next.next
list2.printList()

nd = list1.findIntersection(list2.head)
print(nd.data)

