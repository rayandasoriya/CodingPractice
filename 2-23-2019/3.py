# Given an integer n, return the number of trailing zeroes in n!.
class Solution(object):
    def trailingZeroes(self, n):
        if n == 0:
            return 0
        return n/5+ self.trailingZeroes(n/5)
        
        """
        :type n: int
        :rtype: int
        """
        