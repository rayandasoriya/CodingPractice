def permutation(arr):
    if len(arr)==0:
        return []
    if len(arr)==1:
        return [arr]
    l = []
    for i in range(len(arr)):
        m = arr[i]
        remList = arr[:i]+arr[i+1:]
        for p in permutation(remList):
            if [m]+p not in l:
                l.append([m]+p)
    return l

arr = [1,1,3]
print(permutation(arr))
