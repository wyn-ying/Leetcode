class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        r = x ^ y
        cnt = 0
        while r != 0:
            r = r & (r-1)
            cnt += 1
        return cnt