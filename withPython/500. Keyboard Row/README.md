###idea
此题没有想到什么巧妙的思路，所以直接用了笨办法，用一个dict把每个字母映射成行号，再逐一比较看每个单词的所有字母是否在一行。

###solutions
运用了正则表达式，这是之前没有想到的。代码十分简洁
```python
	return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)
```
###time consuming
#####my solution
65ms-->beats 5.11%
#####discuss solution
59ms-->beats 34.89%