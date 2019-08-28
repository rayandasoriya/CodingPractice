def longestPalindrome(s):
    start_val=0
    max_length=0
    for i in range(len(s)):
        if i-max_length-1>=0 and s[i-max_length-1:i+1]==s[i-max_length-1:i+1][::-1]:
            print("1: ",s[i-max_length-1:i+1])
            start_val=i-max_length-1
            max_length+=2
            print(start_val, max_length)
            
        elif i-max_length>=0 and s[i-max_length:i+1]==s[i-max_length:i+1][::-1]:
            print("2: ",s[i-max_length:i+1])
            start_val=i-max_length
            max_length+=1
    return s[start_val:start_val+max_length]

print(longestPalindrome("malayalam"))