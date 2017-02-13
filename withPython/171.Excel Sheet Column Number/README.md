###idea
简单的10进制转成26进制，从左往右每读一位，乘以26再加上这一位即可，没有什么特别。

复习到的点是python中字符和ascii码互相转换：‘a’-->65，使用```ord('a')```；65-->‘a’，使用```chr(65)```。

最后注意一点是A是从1开始的。

###hot solution
思路一样，不过hot solution使用了```reduce```函数和```lambda```表达式，使得代码非常简洁，也很快。
另外```ord(c)-64```也是一个提醒，可以灵活点不要那么轴，非得```-ord('A')+1```不可。
```python
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return reduce(lambda x, y : x * 26 + y, [ord(c) - 64 for c in list(s)])
```
###time consuming
#####my solution
68ms
#####hot solution
56ms
