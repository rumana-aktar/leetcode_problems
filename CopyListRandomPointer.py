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
## leetcode problem: 138. Copy List with Random Pointer


# # ---------------------------------------------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None
class LinkedList:
    def __init__(self):
        self.head = None
 
    # Method to display the list
    def printList(self):
        print("\nAccording to next: ", end="")
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        
        print("\nAccording to random: ", end="")
        temp = self.head
        while temp:
            if temp.random:
                print(temp.random.data, end=" ")
            else:
                print("null", end=" ")    
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
    
    def pushRandom(self, p1, p2):
        p1.random=p2

    def copyRandomPointer(self):
        # make a copy of each pointer and store in hash 
        head = self.head
        oldToCopy = {None : None}

        cur = head
        while cur:
            copy = Node(cur.data)
            oldToCopy[cur] = copy
            cur = cur.next

        # make the connections among copied pointers
        cur = head
        while cur:
            oldToCopy[cur].next = oldToCopy[cur.next]
            oldToCopy[cur].random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]    
       

# # --------------------------MAIN to TEST-------------------------------------
list2 = LinkedList();
list2.push(7);list2.push(13);list2.push(11); list2.push(10); list2.push(1); 
list2.pushRandom(list2.head, list2.head.next.next.next.next.next)
list2.pushRandom(list2.head.next, list2.head)
list2.pushRandom(list2.head.next, list2.head)
list2.pushRandom(list2.head.next, list2.head)
list2.pushRandom(list2.head.next.next, list2.head.next.next.next.next)
list2.pushRandom(list2.head.next.next.next, list2.head.next.next)
list2.pushRandom(list2.head.next.next.next.next, list2.head)
list2.printList()


ran = LinkedList();
ran.head = list2.copyRandomPointer()

print("\nAfter adding Random Copy Pointers: original Pointers ")
list2.printList()
print("\nAfter adding Random Copy Pointers: copied Pointers ")
ran.printList()

