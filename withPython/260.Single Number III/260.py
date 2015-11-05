class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(nums)
        for i in s:
            nums.remove(i)
        
        for i in nums:
            s.remove(i)
        
        l = list(s)
        
        return l