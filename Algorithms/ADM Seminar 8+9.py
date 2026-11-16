import numpy as np
# %%

# Exercise 2: Simple Operations on lists and arrays
A = []
B = [1,2,3,4,5,6,7,8,9,10,11,12]
C = [3,5,3,6,7,7,1,8,2]

# Order B with even in the front
for i in range(len(B)):
    if B[i] % 2 == 0:
        A.insert(0, B[i])
    else:
        A.insert(len(A), B[i])
print(A)

# Pop last 3 elements of B
for i in range(3):
    B.pop(-1)
    
print(B)

# Pop first 3 elements of B
for i in range(3):
    B.pop(0)
print(B)

# Remove elements of B from C
C = [item for item in C if item not in B]
print(C)

# Arrays
T = np.array([1,2,3,4,5])
D = []

for i in range(len(T)):
    D.append(T[-(i+1)])
print(D)

# %%
# Exercise 3: Shifting the content of an array
import numpy as np

# Define function
def shift_to_right(t):
    first = t[0]
    for i in range(len(t)-1):
        t[i] = t[i+1]
    t[-1] = first
    return t

t = np.array([1,2,3,4,5])
print(shift_to_right(t))



# %%
# Exercise 4: Operations on sets
import numpy as np
# Define function
def intersection(T,S):
    return [item for item in T if item in S]

# Test
T = np.array([1, 17.5, -3, 16, 7]) 
S = {37, 17.5, 4, 13, 41, 16, 9}
print(intersection(T,S))

# Define function union
def union(A,B):
    for item in B:
        A.add(item)
    print(sorted(A))

# Test
A = {-7,5,8,9,13}
B = {2,5,6}
union(A,B)

# Define deleteCommonItems function
def deleteCommonItems(A,B):
    return A - B

# Test
A = {-6.7, 5, 7.1, 21.3, 30}
B = {-7.3, 1.17, 3.45, 6, 7.1, 9.3, 21.3}
print(deleteCommonItems(A,B))




# %%
# Exercise 5: Operations on dictionaries

# Define function intersection
def intersection_dict(A,B):
    return {key: A[key] for key in A if key in B and A[key] == B[key]}

# Test
A = {"John": 33, "Michael": 51, "Delphine": 25, "Chuck": 44}
B = {"Chuck": 44, "Daniela": 73, "Sean": 54, "Michael": 51,"Amy": 42}
print(intersection_dict(A,B))

# Test 2 (empty)
A = {"John": 33, "Michel": 51, "Delphine": 25, "Chuck": 44}
B = {"Chuck": 23, "Daniela": 73, "Sean": 54, "Michael": 51, "Amy": 42}
print(intersection_dict(A,B))

# Define function deleteCommonEntries
def deleteCommonEntries(A,B):
    A = {key: A[key] for key in A if key not in B or A[key] != B[key]}
    return A

# Test
A = {"John": 33, "Michael": 51, "Delphine": 25, "Chuck": 44}
B = {"Chuck": 44, "Daniela": 73, "Sean": 54, "Michael": 51,"Amy": 42}
print(deleteCommonEntries(A,B))
# %%
