# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 22:36:01 2026

@author: Guusd
"""

# Excercise 1 

# Define function
def isPalindrome(s, a, b):
    if a < 0 or a > b:
        print("Invalid (combination of) integer(s)")
    else:
        string = s[a:b+1]        
        return (string == string[::-1])
    
# Test
isPalindrome("abcdeffedcquipopz", 3, 8)



# %% Excercise 2

# Define function
def find_pal(s,k):
    if k < 1:
        print("k needs to be an integer higher than 1")
    else:
        for i in range(len(s) - k + 1):
            if isPalindrome(s, i, k+i-1):
                print(i)
                break
        else:
            print(-1)        


find_pal("abcdeffedcquipopz", 2)