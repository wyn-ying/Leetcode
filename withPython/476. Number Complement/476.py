#solution 1
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # if num << 1 > num:
        max = 1
        while num-max >= 0:
            max = max << 1
        return num ^ (max-1)
        
#solution 2
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # if num << 1 > num:
        max = 1
        while num-max > 0:
            max = (max << 1) + 1
        return num ^ max