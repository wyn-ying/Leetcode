class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        
        r = [1,1]
        for i in range(2,n+1):
            r.append(0)
            for j in range(0,i):
                r[i] += r[j] * r[i-1-j]
        
        return r[n]