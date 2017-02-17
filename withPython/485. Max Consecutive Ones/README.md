###idea
此题比较简单，直接用一个online办法，读到1就将cnt累加，读到0时比较cnt和已有的最长长度比较，更新最长长度，并将cnt清0。

但实现时仍然出现了一个小错误，在bit串读完后，还应该再用cnt更新一下已有的最长长度。

###solutions
思路一样，不过更通顺的逻辑是读到1将cnt累加并更新最长长度，而不是到0再更新。
```python
def findMaxConsecutiveOnes(self, nums):
    cnt = 0
    ans = 0
    for num in nums:
        if num == 1:
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0
    return ans
```
运行速度快了很多
###time consuming
#####my solution
102ms-->beats 54.39%
#####discuss solution
125ms-->beats 23.05%