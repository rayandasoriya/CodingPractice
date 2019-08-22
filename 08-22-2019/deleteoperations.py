import collections
def deleteOperations(arr):
    count = collections.Counter(arr)
    maxi = 0
    for _, value in count.items():
        if value>maxi:
            maxi = value
    return len(arr)-maxi

arr = [1,2,3,4,5]
print(deleteOperations(arr))