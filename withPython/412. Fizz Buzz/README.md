###idea
����ܼ򵥣�һ�������жϾͿ���ʵ�֣�ע�����ж�15��֮�����ж�3��5���ɡ�����д�Ĺ����л���������һ�����⡣һ����û��ע�⵽��1��n������û��ע�⵽����ת�ַ���

###solutions
�����¼һ�������python���룬�����б��Ƶ�ʽֻ��Ҫһ��ʮ�ּ��
```python
return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]
```
ִ���ٶ�Ҳ���жϿ�ܶ�
###time consuming
#####my solution
102ms-->beats 16.30%
#####discuss solution
85ms-->beats 49.35%