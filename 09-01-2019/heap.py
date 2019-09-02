

import heapq
def merge(files):
    files.sort()
    res = 0
    while len(files)>1:
        a = files.pop(files.index(min(files)))
        b = files.pop(files.index(min(files)))
        temp = a+b
        res+= temp
        files.append(temp)
    return res

files = [8, 4, 6, 12]
print(merge(files))