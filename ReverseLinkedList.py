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
## leetcode problem: 0206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []
 

# Constraints:
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000



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

    def reverseLinkedList(self):

        if self.head == None:
            return self.head   

        if self.head.next == None:
            return self.head

        #get the tail
        tail = self.head
        while tail.next:
            tail = tail.next

        # remove cur and insert after tail
        cur = self.head
        while cur != tail:
            temp = cur
            cur =cur.next

            temp.next = tail.next
            tail.next = temp

        self.head = tail    


# # --------------------------MAIN to TEST-------------------------------------
list1 = LinkedList();
list1.push(1);
list1.printList()
list1.reverseLinkedList()
list1.printList()

list2 = LinkedList();
list2.push(1);list2.push(2);list2.push(3); list2.push(4); list2.push(5); list2.push(6);
list2.printList()
list2.reverseLinkedList()
list2.printList()
