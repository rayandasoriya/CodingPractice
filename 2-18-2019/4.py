"""  Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

 Note: The solution set must not contain duplicate triplets.

 For example, given array S = [-1, 0, 1, 2, -1, -4],

 A solution set is:
 [
   [-1, 0, 1],
   [-1, -1, 2]
 ]
 """

def triplets(a):
    a.sort()
    ans = []
    for i in range(len(a)-2):
        if i>0 and a[i-1] == a[i]:
            i+=1
        j = i+1
        k = len(a)-1
        
        while j<k:
            if a[j]+a[k] == -a[i]:
                ans.append([a[i],a[j],a[k]])
                j+=1
                k-=1
                while j<k and a[j] == a[j-1]:
                    j+=1
                while j<k and a[k+1] == a[k]:
                    k-=1
            elif a[j]+a[k]<-a[i]:
                j+=1
            else:
                k-=1
    return ans

S = [-1, 0, 1, 2, -1, -4]
print(triplets(S))