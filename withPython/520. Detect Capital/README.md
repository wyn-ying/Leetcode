###idea
用python的isupper和islower函数可以简单实现功能。
逻辑如下：将字符串分成第一个字母和除第一个字母的子串。对于子串，若不全为大写或全为小写，一定为False；若全为大写，看第一个字母若为小写，则为False；其他情况都是True。
###solutions
如果再用上python的istitle函数：
```python
return word.isupper() or word.islower() or word.istitle()
```
效率差不多。
###time consuming
#####my solution
58ms-->beats 52.53%
#####discuss solution
59ms-->beats 45.25%