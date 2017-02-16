###idea
此题比较简单。对于每个是island的块，若它相邻的四个块中有x块island，则这一块对周长的贡献就是4-x。最后遍历所有的块即可。
一次写对。
###solutions
简洁版python代码
```python
	return sum(sum(map(operator.ne, [0] + row, row + [0]))
               for row in grid + map(list, zip(*grid)))
```
思路是：若相邻两块的值不一样，则意味着一块是水一块是陆地，那么这样的pair意味着中间有一条线为周长贡献了1。只需要横向和纵向遍历所有的pair即可。
但这样做的执行效率没有明显提高。
###time consuming
#####my solution
309ms-->beats 55.91%
#####discuss solution
342ms-->beats 30.46%