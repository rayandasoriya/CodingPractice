def decode(s):
    dp = [0]*(len(s)+1)
    dp[0] = 1
    if s[0] == '0':
        dp[1] = 0
    else:
        dp[1] = 1
    for i in range(2,len(s)+1):
        oneDigit = int(s[i-1:i])
        twoDigit = int(s[i-2:i])
        if oneDigit>=1:
            dp[i] += dp[i-1]
        if twoDigit>=10 and twoDigit<=26:
            dp[i] += dp[i-2]
    return dp[len(s)]

print(decode("226"))