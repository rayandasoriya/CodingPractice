import collections
def numSubarraysWithSum(A, S):
    res=0
    sum_dict={0:1}
    cursum=0
    for i in A:
        cursum+=i
        if cursum-S in sum_dict:
            res+=sum_dict[cursum-S]
        if cursum in sum_dict:
            sum_dict[cursum]+=1
        else:
            sum_dict[cursum]=1
        print(cursum, res)
    print(sum_dict)
    return res

A = [1,0,1,0,1,0,0,0,0,1]
S = 3
print(numSubarraysWithSum(A,S))