class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = nums[0]
        sum = tmp = 0
        for i in nums:
            tmp += i
            if tmp > sum:
                sum = tmp
            elif tmp < 0:
                tmp = 0
            if i > max:
                max = i
        if max > 0:
            return sum
        else:
            return max