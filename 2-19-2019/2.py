""" Given an array of integers, find if the array contains any duplicates. Your function should return 
true if any value appears at least twice in the array, and it should return false if every element is distinct.
 """

from collections import Counter

def duplicate(a):
    cou = Counter(a)
    for (key,value) in cou.items():
        if value>1:
            return True
    return False

a = [1,2,3,4,5,6,7]
print(duplicate(a))