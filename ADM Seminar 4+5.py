# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:22:39 2026

@author: Guusd
"""


#%%  Excercise 1 Character in a string
character = 'l'
string = 'algorithmics'

# Define function
def CharacterCheck(character, string):
    check = string.find(character) + 1
    if check > 0:
        print(check)
    else:
        print(False)

# Test    
CharacterCheck(character, string)    

# Test different values
character2 = 'b'
CharacterCheck(character2, string)


# %% Excercise 2 Palindrome
S = 'coloc'

# Define function
def PalindromeCheck(string):
    print(string == string[::-1])
    print(string[::-1]) # Print reversed value for fun
    
# Test
PalindromeCheck(S)

# Test different values
S2 = 'Hello World!'
PalindromeCheck(S2)

#%% Excercise 3 Perfect Number

# Define function
def PerfectCheck(number):
    total = 0
    for i in range(1,number): # Loop through possible numbers
        if number % i == 0:
            total = total + i # Sum if number is divisible by i
    print(total == number) # Check if perfect and print result

# Test
PerfectCheck(6)
PerfectCheck(7)

