###hot solution
python�ļ����ѧ�����ϴ��룺
```python
class Solution(object):
    def moveZeroes(s, a):
        a.sort(key=lambda x: not x or None)
```
�Լ����ĸ����棺
```python
def moveZeroes(self, nums):
    nums.sort(key=operator.not_)
```
˼·��ͨ�� not x����0Ԫ�ص�keyΪ0��0��keyΪ1������sort֮���0Ԫ�ض��ŵ���ǰ�档

###time comsuming
#####my solution
124ms
#####hot solution
68ms