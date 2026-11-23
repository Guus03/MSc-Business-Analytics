# %%
# Exercise 1, make algorithm that checks array for duplicates.

def has_duplicates(arr):
    seen = set()
    for item in arr:
        if item in seen:
            return True
        seen.add(item)
    return False

# Test the function
print(has_duplicates([2,3,3,4,5]))  # True
print(has_duplicates([2,6,3,4,5]))  # False

# %%
# Exercise 2, algorithm that uses dictionary to return position of characters in list d, if not found return -1.
def position_marker(d,q):
    dictionary = {}
    for i, word in enumerate(d):
        if word not in dictionary:
            dictionary[word] = i
    
    # Check q in d and return value
    results = []
    for word in q:
        if word in dictionary:
            results.append(dictionary[word])
        else:
            results.append(-1)
    print(results)
    return results

# Test algorithm
d = ["the", "evening", "and", "the", "morning", "the", "sky", "is", "blue", "and", "pink"]
q = ["morning", "the", "green", "sky"]

# test
position_marker(d,q)