###idea
����ÿһԪ�أ�ֻҪ��һԪ�ر����󣬾��������׬������Ϊ��ֵ������list���ɡ�

###hot solution
˼·���ƣ�����hot solution�Ĵ𰸸���ࡣ���֮��my solution�Եúܱ�׾����Ҫ������listʹ�����档
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