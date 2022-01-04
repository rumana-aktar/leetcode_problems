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
## leetcode problem: 709. To Lower Case

# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

# Example 1:
# Input: s = "Hello"
# Output: "hello"

# Example 2:
# Input: s = "here"
# Output: "here"

# Example 3:
# Input: s = "LOVELY"
# Output: "lovely"

# Constraints:
# 1 <= s.length <= 100
# s consists of printable ASCII characters.

# # ---------------------------------------------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()



def convertToLowerCase(s):
    s=list(s)

    for i in range(len(s)):
        if s[i] >= 'A' and s[i] <='Z':
            s[i]= chr(ord(s[i]) + 32)      

    return ''.join(s)


# # --------------------------MAIN to TEST-------------------------------------
print(convertToLowerCase("Hello"))
print(convertToLowerCase("LOVELY"))
print(convertToLowerCase("here"))
print(convertToLowerCase("I Love You"))
