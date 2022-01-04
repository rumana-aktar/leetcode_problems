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
## leetcode problem: 0141. Linked List Cycle 

# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.


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

    def push(self, val):
        node = Node(val)
        if self.head == None:
            self.head=node
            return
        
        cur=self.head
        while cur.next:
            cur=cur.next
        cur.next=node


    # if we set two pointers, slow (moves one right each iteration) and fast (moves two right each iteration); they will meet at some point if there is a cycle in the linkedlist; 
    #if not, they will reach tail
    def hasCycle(self):
        fast = self.head
        slow = self.head

        if slow == None:
            return False

        i=0
        while fast and fast.next:
            if slow == fast and i != 0:
                return True
            fast = fast.next.next 
            slow = slow.next
            i += 1

        return False    


# # --------------------------MAIN to TEST-------------------------------------
list1 = LinkedList();
list1.push(3);list1.push(2);list1.push(0); list1.push(-4)
list1.head.next.next.next.next = list1.head.next
print(list1.hasCycle())

list1 = LinkedList();
list1.push(1);list1.push(2);
list1.head.next.next = list1.head
print(list1.hasCycle())

list1 = LinkedList();
list1.push(1);
print(list1.hasCycle())


 