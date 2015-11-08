###idea
题目有不让用除法和线性时间复杂度的限制，第一遍做的时候没有想出来。
看了hot solution后感觉是因为对动态规划（DP）不太熟。
现在对DP应用场景又加深了一些了解。

###hot solution
```python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output
```
思路：可以算作是动态规划的解法。
首先建立一个输出列表，
从前到后，把每个元素前面的部分求乘积，存进去；
之后倒过来，把每个元素后面的数的乘积再乘进去。

###time consuming
#####hot solution
188ms