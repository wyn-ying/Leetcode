###hot solution
python的简洁哲学，先上代码：
```python
class Solution(object):
    def moveZeroes(s, a):
        a.sort(key=lambda x: not x or None)
```
以及它的更简洁版：
```python
def moveZeroes(self, nums):
    nums.sort(key=operator.not_)
```
思路：通过 not x，非0元素的key为0，0的key为1。于是sort之后非0元素都排到了前面。

###time comsuming
#####my solution
124ms
#####hot solution
68ms