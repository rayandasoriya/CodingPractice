def greatest(arr):
    max_n = arr[len(arr)-1]
    arr[len(arr)-1] = -1
    for i in range(len(arr)-2,-1,-1):
        temp = arr[i]
        arr[i] = max_n
        if temp>max_n:
            max_n = temp
    return arr

arr = [16, 17, 4, 3, 5, 2]
print(greatest(arr))