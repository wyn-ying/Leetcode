class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        cnt = 0
        for i in nums:
            if target > i:
                cnt += 1
            else:
                return cnt
                
        return cnt