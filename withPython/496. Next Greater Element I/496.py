class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        l=len(nums)
        r=list()
        for num in findNums:
            i=0
            for _ in range(l):
                if nums[i] == num:
                    break
                i+=1
            g=-1
            for j in range(i+1, l):
                if nums[j]>num:
                    g = nums[j]
                    break
            r.append(g)
        return r