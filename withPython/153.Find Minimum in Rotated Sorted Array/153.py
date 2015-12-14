class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min = nums[0]
        head = nums[0]
        for i in nums:
            if i < head and i < min:
                min = i
        
        return min