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
## leetcode problem: 0083. Remove Duplicates from Sorted List
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the list sorted as well.

# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]

# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3] 

# Constraints:
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.


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

    # to build thee linkedlist
    def push(self, val):
        node = Node(val)
        if self.head == None:
            self.head=node
            return
        
        cur=self.head
        while cur.next:
            cur=cur.next
        cur.next=node

    def deleteDuplicates(self,head):
        
        if head == None:
            return head

        cur=head
        while cur.next:
            if cur.data == cur.next.data: #seen before, so skip it
                cur.next=cur.next.next
            else:
                cur=cur.next
        return head        
    
# # --------------------------MAIN to TEST-------------------------------------
list1 = LinkedList();
list1.push(1);list1.push(1);list1.push(2);list1.push(3);list1.push(3);list1.push(3);
list1.printList(); 
list1.deleteDuplicates(list1.head)
list1.printList(); 


list2 = LinkedList();
list2.push(1);list2.push(1);list2.push(2);list2.push(2);list2.push(2);list2.push(3); list2.push(4);list2.push(4);list2.push(5);list2.push(6);
list2.printList()
list2.deleteDuplicates(list2.head)
list2.printList(); 

list2 = LinkedList();
list2.printList()
list2.deleteDuplicates(list2.head)
list2.printList(); 
