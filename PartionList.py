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
## leetcode problem: 86. Partition List

# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.

# Example 1:
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]

# Example 2:
# Input: head = [2,1], x = 2
# Output: [1,2]
 

# Constraints:
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200


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

    def partion(self, x):
        if self.head == None:
            return
        if self.head.next == None:
            return

        dummy = Node(0)
        dummy.next = self.head
        cur = dummy.next
        sml = dummy

        # reach x
        while cur and cur.data != x:
            if cur.data < x:
                sml = sml.next
            cur = cur.next

        # from cur, consider each element wether it is smaller than x and needed to move after sml
        while cur.next:
            if cur.next.data < x:
                temp = cur.next
                cur.next = temp.next
                temp.next = sml.next
                sml.next = temp

                sml = sml.next
            else:
                cur = cur.next

        self.head = dummy.next        


# # --------------------------MAIN to TEST-------------------------------------
list2 = LinkedList();
list2.push(3);list2.push(4); list2.push(6);list2.push(1); list2.push(2); list2.push(5); list2.push(6);
list2.printList()
list2.partion(3)
list2.printList()
