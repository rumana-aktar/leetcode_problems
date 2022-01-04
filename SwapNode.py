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
## leetcode problem: 0024. Swap Nodes in Pairs

#Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in 
# the list's nodes (i.e., only nodes themselves may be changed.)

# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

# Example 2:
# Input: head = []
# Output: []

# Example 3:
# Input: head = [1]
# Output: [1]


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


    def swapNode(self):
        dummy=Node(0)
        dummy.next=self.head
        self.head=dummy

        # add a dummy and swap next two nodes and keep going
        cur=dummy
        while cur and cur.next and cur.next.next:
            temp=cur.next
            cur.next=cur.next.next
            temp.next=cur.next.next
            cur.next.next=temp
            cur=cur.next.next

        self.head=dummy.next


# # --------------------------MAIN to TEST-------------------------------------
list1 = LinkedList();
list1.push(1);list1.push(2);list1.push(4);
list1.printList(); 
list1.swapNode()
list1.printList()

list2 = LinkedList();
list2.push(1);list2.push(3);list2.push(4); list2.push(14); list2.push(43);list2.push(45);
list2.printList()
list2.swapNode()
list2.printList()


list1 = LinkedList();
list1.push(1);
list1.printList(); 
list1.swapNode()
list1.printList()

list1 = LinkedList();
list1.printList(); 
list1.swapNode()
list1.printList()