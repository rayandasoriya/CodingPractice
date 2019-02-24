def maxproduct(a):

    maxe,mine,max_s = 1,1,1

    for i in range(len(a)):
        if a[i]>0:
            maxe = maxe*a[i]
            mine = min(mine*a[i],1)
        elif a[i] == 0:
            maxe = 1
            mine = 1
        else:
            temp = maxe
            maxe = max(mine*a[i],1)
            mine = temp*a[i]
        if max_s < maxe:
            max_s = maxe

    return max_s




a = [1, -2, -3, 0, 7, -8, -2]
print(maxproduct(a))