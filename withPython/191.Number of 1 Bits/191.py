class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = 0
        while n > 0:
            if n % 2:
                r = r + 1
            n = n / 2
        
        return r