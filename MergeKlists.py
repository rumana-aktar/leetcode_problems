# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %  Solution Author: Rumana Aktar 
# %  Date: 01/05/2022
# %
# %  For more information, contact:
# %      Rumana Aktar
# %      226 Naka Hall (EBW)
# %      University of Missouri-Columbia
# %      Columbia, MO 65211
# %      rayy7@mail.missouri.edu
# # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



## leetcode problem:

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()
import heapq

def mergeKlists(lists):
    k = len(lists)
    heap_el = []
    head = []
    res = []
    for i in range(k):
        heap_el.append([lists[i][0], i])
        head.append(1)
            
            
    # build the heap with first element of all lists    
    #print(heap_el)
    heapq.heapify(heap_el)   
    #print(heap_el)

    while len(heap_el) > 0:
        ext_min, list_no = heapq.heappop(heap_el)
        res.append(ext_min)
        
        if head[list_no] < len(lists[list_no]) :
            #print([lists[list_no], head[list_no], lists[list_no][head[list_no]]])
            heapq.heappush(heap_el, [lists[list_no][head[list_no]], list_no])
            head[list_no] = head[list_no] + 1


    return res
# # --------------------------MAIN to TEST-------------------------------------
lists = [[1,4,5],[7,8],[1,3,4],[2,6]]
print(mergeKlists(lists))

# # --------------------------MAIN to TEST-------------------------------------
