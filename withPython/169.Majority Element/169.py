class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        halflength = len(nums)/2
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        
        for key, item in dic.items():
            if item > halflength:
                return key