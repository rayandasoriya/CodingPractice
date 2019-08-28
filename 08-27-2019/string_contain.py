def contain(s,p):
    count = 0
    for i in range(len(s)):
        if s[i] == p[count]:
            count+=1
            if count==len(p):
                return True
    return False

print(contain("rayan", "riy"))