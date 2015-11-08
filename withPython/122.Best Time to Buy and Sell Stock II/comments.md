###idea
对于每一元素，只要后一元素比它大，就有利润可赚，利润为差值。遍历list即可。

###hot solution
思路类似，不过hot solution的答案更简洁。相比之下my solution显得很笨拙，主要问题在list使用上面。
```python
class Solution(object):
    def maxProfit(self, prices):
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))
```

###time comsuming
#####my solution
48ms
#####hot solution
64ms