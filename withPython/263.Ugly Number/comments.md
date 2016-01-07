被这个题卡了好久，间歇性又有考试等纠缠，所以拖了很久。我的代码对较小的数判断应该都没有问题，但被一个变态的case -2147483648卡住。
实在想不出优雅的办法搞定。所以就这样了……
###idea
顺序找出小于num的质数，让num依次除，发现除去2，3，5的质因子就说明不是ugly number。
###hot solution
看了python代码，发现人家对小于0的全部判断为false。这点是之前没考虑到的。
之后，在我的代码中加入这条判断后，case 214797179仍然不能通过，应该是使用了list的缘故。
```python
def isUgly(self, num):
    """
    :type num: int
    :rtype: bool
    """
    if num <= 0:
        return False
    for x in [2, 3, 5]:
        while num % x == 0:
            num = num / x
    return num == 1
```
###time consuming
#####hot solution
52ms-->89.66%