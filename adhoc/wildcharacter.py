# Match WildCharacters * and ?
# Question:
# The wildcard pattern can include the characters ‘?’ and ‘*’
# ‘?’ – matches any single character
# ‘*’ – Matches any sequence of characters (including the empty sequence)

# Sources:
# 1. https://practice.geeksforgeeks.org/problems/wildcard-pattern-matching/1
# 2. https://www.hackerrank.com/contests/placement-preparation-1/challenges/string-matching-with-wildcards/problem

pattern = str(raw_input())
string = str(raw_input())
pattern = pattern.strip()
string = string.strip()
def wildCard(str1, str2):
    if not str1 and not str2:
        return True
    if not str2:
        for char in str1:
            if char != "*":
                return False
        return True
    if not str1:
        return False
    
    if str1[0] == "?":
        return wildCard(str1[1:], str2[1:])
    elif str1[0] == "*":
        return wildCard(str1[1:], str2) or wildCard(str1[1:], str2[1:]) or wildCard(str1, str2[1:])
    else :
        return_val = str1[0]==str2[0] and wildCard(str1[1:], str2[1:])
        return return_val
 
print str(wildCard(pattern, string)).upper()
