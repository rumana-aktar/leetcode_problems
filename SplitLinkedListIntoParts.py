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
## leetcode problem: 0725. Split Linked List in Parts


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
        print("\n")
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


    def splitLinkedListIntoParts(self, k):
        
        # get the node counts
        cur=self.head
        count =0
        while cur:
            count += 1
            cur = cur.next

        node_no_per_list = count // k
        extra_nodes = count % k
        
        # generate empty lists for returing the linkedList parts
        res = [node_no_per_list + 1] * extra_nodes + [node_no_per_list] * (k-extra_nodes)
 
        # cur is the head of each part
        prev, cur = None, self.head
        for i, num in enumerate(res):
            if prev:
                prev.next=None

            res[i]=cur
            for j in range(num):
                prev, cur = cur, cur.next
        return res            
        

# # --------------------------MAIN to TEST-------------------------------------
list1 = LinkedList();
list1.push(1);list1.push(3);list1.push(4); 
list1.printList()
res=list1.splitLinkedListIntoParts(5)

# print the parts
for x in res:
    print("\nPart: ", end="")  
    temp = x
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    

list2 = LinkedList();
list2.push(1);list2.push(3);list2.push(4); list2.push(14); list2.push(43);
list2.printList()
res=list2.splitLinkedListIntoParts(3)

# print the parts
for x in res:
    print("\nPart: ", end="")  
    temp = x
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    

