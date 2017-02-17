class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=0
        max=0
        for i in nums:
            if i==0:
                if cnt>max:
                    max=cnt
                cnt=0
            else:
                cnt+= 1
        if cnt>max:
            max=cnt
        return max