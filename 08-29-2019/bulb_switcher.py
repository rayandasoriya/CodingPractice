def switcher(n):
    arr = [0]*n
    for i in range(n):
        if i == 0:
            arr = [1]*n
        elif i == 1:
            for j in range(i,n,2):
                arr[j] = 0
        else:
            for j in range(i,n,i):
                if arr[j] == 1:
                    arr[j] = 0
                else:
                    arr[j] = 1
        print(i,arr)

    print(arr)
    return arr.count(1)


print(switcher(3))