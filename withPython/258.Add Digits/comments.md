###hot solution

#####idea��Ҫ���á����ս��ֻʣ1λ����Ҫ���Լ�����9�����ԡ�

�Ƚ�0������������ǡ�

֮����һ���������һ���������Ϊ������numΪ9�ı����������9�����ʣ��ӵ�1λ��ʱ�ض�Ϊ9��
���������֮������num%9������⡣
��Ҫע����ǣ���numΪ9�ı�����num%9�����0������9�������Ҫ�����г�num%9==0�������

������hot solution���룺

```python
def addDigits(self, num):
    if num==0:
        return 0
    if num%9==0:
        return 9
    return num%9
```

�������������ԣ������и����ĸĽ��汾��

```python
def addDigits(self, num):
	return num % 9 or num and 9
```