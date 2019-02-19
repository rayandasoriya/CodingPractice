""" Given an input string, reverse the string word by word.
For example,
Given s = "the sky is blue",
return "blue is sky the".
"""
def revstring(a):
    a = a.split(" ")
    m = []
    str_len = len(a)-1
    for i in range(str_len,-1,-1):
        m.append(a[i])
    return m

print revstring("The sky is blue")
