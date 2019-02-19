# Given an array of size n, find the majority element. The majority element is the element that appears more than n/2  times.

from collections import Counter

def count_element(a):
    count_e = Counter(a)
    for (key,val) in count_e.items():
        if val>len(a)/2:
            return key
    return -1

a = [1,2,3,4,5,5,5,5,5,5,5]
print(count_element(a))

a = [1,2,3,4,5,5,5]
print(count_element(a))
