class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        
        for i in nums:
            if i == 0:
                cnt = cnt + 1
        
        if cnt>0:    
            for i in range(0,cnt):
                nums.remove(0)
                nums.append(0)