class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n==2:
            return 2
        else:
           record = [1,2]
           i = 3
           while i <= n:
               record.append(record[i-2]+record[i-3])
               i += 1
           return record[n-1]