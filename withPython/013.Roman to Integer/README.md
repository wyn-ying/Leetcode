###idea
没什么新鲜的，基本都是字符串的操作，因此不同语言差别比较大，所以没有实际写，大概想了一下。

这个题目比较适合用python做，因为字符串处理是python的强项。最早想到了字典，之后一个字符一个字符读进来，对应加和就可以了。
但是比较没想清楚的地方是对于IV，IX这样小单位在大单位前面的怎么处理。
比较笨的办法是匹配两位的，之后扔掉再处理都是一位的。

###hot solution
基于python语言比较巧妙的办法。如果前面一个单位比后面一个单位小，就用减法，否则加。这也符合罗马数字最初的设计思路。
```python
class Solution:
# @param {string} s
# @return {integer}
def romanToInt(self, s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]
```
###time consuming
#####hot solution
172ms-->55.59%