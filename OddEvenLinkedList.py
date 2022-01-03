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
## leetcode problem: 328. Odd Even Linked List 

# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]

# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]



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



    def oddEven(self):
        if self.head == None:
            return
        if self.head.next == None:
            return     

        odd = self.head
        even= odd.next

        while even and even.next:
            temp = even.next
            even.next = even.next.next
            temp.next = odd.next
            odd.next = temp

            odd = odd.next
            even = even.next


# # --------------------------MAIN to TEST-------------------------------------
list1 = LinkedList();
list1.push(2); list1.push(1); list1.push(3); list1.push(5); list1.push(6);  list1.push(4);     list1.push(7);           
list1.printList()
list1.oddEven()
list1.printList()            

# # --------------------------MAIN to TEST-------------------------------------
list2 = LinkedList();
list2.push(1);list2.push(2);list2.push(3); list2.push(4); list2.push(5); list2.push(6);
list2.printList()
list2.oddEven()
list2.printList()
