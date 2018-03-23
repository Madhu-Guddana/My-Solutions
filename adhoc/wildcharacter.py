# Match WildCharacters * and ?
# Question:
# The wildcard pattern can include the characters ‘?’ and ‘*’
# ‘?’ – matches any single character
# ‘*’ – Matches any sequence of characters (including the empty sequence)
# Print True if pattern matches the string, False otherwise.

# Sources:
# 1. https://practice.geeksforgeeks.org/problems/wildcard-pattern-matching/1
# 2. https://www.hackerrank.com/contests/placement-preparation-1/challenges/string-matching-with-wildcards/problem

# The recursive Program is self explanatory.

pattern = str(raw_input())
string = str(raw_input())
pattern = pattern.strip()
string = string.strip()
def wildCard(pattern, string):
    
    # Case where both are empty.
    if not pattern and not string:
        return True
    
    # Case where String is empty, then pattern must be full of '*' char.
    if not string:
        for char in pattern:
            if char != "*":
                return False
        return True
    
    # Case where string is not empty but pattern is empty.
    if not pattern:
        return False
    
    if pattern[0] == "?":
        return wildCard(pattern[1:], string[1:])
    elif pattern[0] == "*":
        # Case          * consumes 0 char                * consumes 1 char              * consumes more than 1 char.
        return wildCard(pattern[1:], string) or wildCard(pattern[1:], string[1:]) or wildCard(pattern, string[1:])
    else :
        return_val = pattern[0] == string[0] and wildCard(pattern[1:], string[1:])
        return return_val
 
print str(wildCard(pattern, string)).upper()
