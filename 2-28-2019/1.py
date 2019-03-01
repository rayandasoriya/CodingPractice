def longest_uncommon(a):
    i = 1
    c_len = 1
    max_len = 1
    prev = 0
    n = len(a)
    visited= [-1] * 256
    visited[ord(a[0])] = 0
    for i in range(1,n):
        prev = visited[ord(a[i])]
        if prev == -1 or (i-c_len>prev):
            c_len+=1
        else:
            if c_len>max_len:
                max_len = c_len
            c_len = i-prev
        
        visited[ord(a[i])] = i
        if c_len>max_len:
                max_len = c_len
    return max_len

a = "abcdva"
print(longest_uncommon(a))