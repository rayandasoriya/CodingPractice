def cons(s,k):
    dp = [0]*len(s)
    dp[0] = 1
    for i in range(1,len(s)):
        if s[i-1] == s[i]:
            dp[i] = dp[i-1]+1
        else:
            dp[i] = 1
    new_str = ""
    i = len(dp)-1
    while i>=0:
        if dp[i]<k:
            new_str = s[i]+new_str
            i-=1
        else:
            i-=k
    return new_str

s = "aabbbac"
k = 3
print(cons(s,k))