""" Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:
Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime? """


def digit(a):
    sum = 0
    while a>0:
        rem = a%10
        sum+=rem
        a = a/10
    return sum


def digit2(n):
    if n==0:
        return 0
    if n%9==0:
        return 9
    else:
        return n%9

print digit2(123)