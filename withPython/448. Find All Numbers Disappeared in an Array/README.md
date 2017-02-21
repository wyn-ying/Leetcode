###idea
要求不使用额外空间，并且线性时间得到结果。没有什么好思路，于是写了一个pythonic的代码。

思路：直接用set的difference函数暴力求出set(range)和set(nums)的差别。

###hot solution
通过把每个数作为序号对应的那个数改成负数，O(n)时间可以把list扫描一遍，在list中存在的数，它们作为下标在list中的数都被改成了负数，那么list中是正数的对应的数就是miss的。

很巧妙地利用了数组下标和正负号做标记。就是速度偏慢。
```python
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        idx=0
        for i in xrange(len(nums)):
            idx=abs(nums[i])-1
            nums[idx] = -abs(nums[idx])
        return [i+1 for i in range(len(nums)) if nums[i]>0]
```
###time consuming
#####my solution
272ms-->beats 90.14%
#####hot solution
349ms-->beats 53.56%