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



## leetcode problem: 290 Word Pattern
# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
 

# Constraints:

# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.

# # --------------------------Solution-------------------------------------
import os; 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear'); clearConsole()


def wordPattern(pattern, s):
    words = s.split()
    d={}
    d2={}

    if len(words) != len(pattern):
        return False

    i=0
    while i < len(pattern):
        p = pattern[i]

        # both pattern and word is new
        if p not in d and words[i] not in d2:
            d[p] = words[i]
            d2[words[i]] = p

        # pattern already appeared before
        elif p in d:
            if d[p] != words[i]:
                return False

        # word already appeared before
        elif words[i] in d2:
            if d2[words[i]] != p:
                return False

        i += 1

    return True

        

# # --------------------------MAIN to TEST-------------------------------------
pattern = "abba"; s = "dog cat cat dog"
print(wordPattern(pattern, s))
# # --------------------------MAIN to TEST-------------------------------------
pattern = "abba"; s = "dog cat cat fish"
print(wordPattern(pattern, s))
# # --------------------------MAIN to TEST-------------------------------------
pattern = "aaaa"; s = "dog cat cat dog"
print(wordPattern(pattern, s))
