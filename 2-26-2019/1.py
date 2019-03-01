from collections import Counter
from collections import OrderedDict

def first_uncommon(a):
    # time complexity = O(n)
    a = a.lower()
    for i in a:
        if a.count(i) == 1:
            return i
    return -1

def ordered_string(a):
    # time complexity = O(nLgn)
    a = a.lower()  
    fi = []
    d = OrderedDict()   #To maintain the order while inserting
    for i in a:
        d[i] = a.count(i)   #creating the ordereddict
    value_sort = sorted(d.items(), key=lambda k: k[1])   #Sort the dict while maintaining the relative order
    for key,value in value_sort:
        fi.append(key*value)
    return "".join(fi) if fi else -1

a = raw_input("Enter the string: ")

print(first_uncommon(a))
print(ordered_string(a))