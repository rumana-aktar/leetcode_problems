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
## leetcode problem: 61. Rotate List

# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]


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

    def rotateByK(self, k):
        
        # get the count and tail node
        count = 0
        cur = self.head
        tail = self. head
        while cur:
            count += 1
            tail = cur
            cur=cur.next

        k=k%count
        if k==0:
            return

        # move to (count-k)th node
        d = count - k
        cur= self.head
        newTail=cur
        while d and cur:
            newTail=cur
            cur = cur.next
            d -= 1

        # set the new tail's next to null
        newTail.next=None
        # link the original  tail and head
        tail.next=self.head
        # make current node the new head
        self.head=cur


# # --------------------------MAIN to TEST-------------------------------------
list1 = LinkedList();
list1.push(1);list1.push(2);list1.push(4);
list1.printList(); 
list1.rotateByK(1)
list1.printList(); 


list2 = LinkedList();
list2.push(1);list2.push(3);list2.push(4); list2.push(14); list2.push(43);list2.push(45);
list2.printList()
list2.rotateByK(16)
list2.printList(); 
