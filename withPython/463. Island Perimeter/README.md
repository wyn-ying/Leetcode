###idea
����Ƚϼ򵥡�����ÿ����island�Ŀ飬�������ڵ��ĸ�������x��island������һ����ܳ��Ĺ��׾���4-x�����������еĿ鼴�ɡ�
һ��д�ԡ�
###solutions
����python����
```python
	return sum(sum(map(operator.ne, [0] + row, row + [0]))
               for row in grid + map(list, zip(*grid)))
```
˼·�ǣ������������ֵ��һ��������ζ��һ����ˮһ����½�أ���ô������pair��ζ���м���һ����Ϊ�ܳ�������1��ֻ��Ҫ���������������е�pair���ɡ�
����������ִ��Ч��û��������ߡ�
###time consuming
#####my solution
309ms-->beats 55.91%
#####discuss solution
342ms-->beats 30.46%