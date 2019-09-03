def great(arr):
    ans = []
    max_l = float('-inf')
    for i in range(len(arr)-1,-1,-1):
        if arr[i]>max_l:
            max_l = arr[i]
            ans.insert(0,max_l)
    return ans

print(great([16,18,6,7,4,1]))