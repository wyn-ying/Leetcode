class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            dic[i]=dic.get(i, 0) + 1
        
        for key, items in dic.items():
            if items == 1:
                return key