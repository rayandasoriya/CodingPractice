import collections
def permutation(s1,s2):
    c1 = collections.Counter(list(s1))
    c2 = collections.Counter(list(s2))
    return c1 == c2

c1 = "rayan"
c2 = "Rayan"
print(permutation(c1,c2))
