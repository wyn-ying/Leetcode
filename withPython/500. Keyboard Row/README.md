###idea
����û���뵽ʲô�����˼·������ֱ�����˱��취����һ��dict��ÿ����ĸӳ����кţ�����һ�ȽϿ�ÿ�����ʵ�������ĸ�Ƿ���һ�С�

###solutions
������������ʽ������֮ǰû���뵽�ġ�����ʮ�ּ��
```python
	return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)
```
###time consuming
#####my solution
65ms-->beats 5.11%
#####discuss solution
59ms-->beats 34.89%