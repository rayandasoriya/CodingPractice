# Given two strings S and T, determine if they are both one edit distance apart.


def one_edit(s,d):
    for i in range(min(len(s),len(d))):
        if(s[i]!=d[i]):
            if len(s) == len(d):
                return s[i+1]==d[i+1]
            elif len(s)<len(d):
                return s[i]==d[i+1]
            else:
                return s[i+1]==d[i]
    return abs(len(s)-len(d))==1

s = "Helloyde"
d = "Helloy"
print(one_edit(s,d))