###idea
和013基本一样。最简单也最快的思路就是做4组字典，个位到千位，之后查字典输出。

###hot solution
最高票答案的思路跟我开始想的基本一样。
```java
public static String intToRoman(int num) {
    String M[] = {"", "M", "MM", "MMM"};
    String C[] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
    String X[] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
    String I[] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
    return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10];
}
```
至于python代码版本就多了。有[用replace的](https://leetcode.com/discuss/25519/an-accepted-answer-in-python-using-s-replace)，也有1459特殊处理的。

下面贴一个1459处理的：
```python
def intToRoman(self, num):
    """
    :type num: int
    :rtype: str
    """
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    res = ""
    for i, v in enumerate(values):
        res += (num//v) * numerals[i]
        num %= v
    return res
```
但跑下来发现还是查字典的方法最快，虽然看起来有点丑陋。

###time consuming
#####my solution
112ms-->94.75%
#####hot solution
136ms-->47.24%