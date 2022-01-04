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
## leetcode problem: 0020. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false
 

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# # ---------------------------------------------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()


from collections import deque
def bracketMatching(s):
    st=deque()
    
    # for quick search, store the bracket pairs in a dictionary
    d={}
    d['(']=')';     d['{']='}';     d['[']=']'

    for ch in s:
        if ch == '(' or ch == '{' or ch =='[': #if opening bracket, push at top of stack
            st.append(ch)
        
        elif ch == ')' or ch =='}' or ch == ']': #if closing, pop from the top of the stack
            if len(st) == 0:
                return False

            top=st.pop()
            if d[top] != ch :
                return False    
    
    # if the stack is nonempty, then there is atleast one opening bracket left in the stack
    if len(st) > 0:
        return False

    return True

# # --------------------------MAIN to TEST-------------------------------------
print(bracketMatching("{()}()"))            
print(bracketMatching("{()()"))            