def wordBreak(s, wordDict):
    dp = [False]*(len(s)+1)
    dp[0] = True
    for i in range(len(s)+1):
        for j in wordDict:
            if dp[i-len(j)] and s[i-len(j):i] == j:
                dp[i] = True
                break
    return dp[len(s)]
print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))