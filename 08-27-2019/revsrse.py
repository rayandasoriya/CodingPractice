def reverse(s):
    s = list(s)
    l = 0
    r = len(s)-1
    while l<r:
        s[l],s[r] = s[r],s[l]
        l+=1
        r-=1
    return "".join(s)

s = ""
print(reverse(s))