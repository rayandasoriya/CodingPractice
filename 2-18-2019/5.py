""" // Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

 Note:
     You must do this in-place without making a copy of the array.
     Minimize the total number of operations.
 """
def zeroes(a):
    index=0
    for i in a:
        if i!=0:
            a[index]=i
            index+=1
    while index<len(a):
        a[index]=0
        index+=1
    return a
    
nums = [0, 1, 0, 3, 12]
print(zeroes(nums))