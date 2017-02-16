###idea
此题很简单，一组条件判断就可以实现，注意先判断15，之后再判断3和5即可。但在写的过程中还是遇到了一点问题。一个是没有注意到从1到n，二是没有注意到数字转字符。

###solutions
这里记录一个经典的python代码，用了列表推导式只需要一行十分简洁
```python
return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]
```
执行速度也比判断快很多
###time consuming
#####my solution
102ms-->beats 16.30%
#####discuss solution
85ms-->beats 49.35%