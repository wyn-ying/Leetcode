###idea
��Ŀ�в����ó���������ʱ�临�Ӷȵ����ƣ���һ������ʱ��û���������
����hot solution��о�����Ϊ�Զ�̬�滮��DP����̫�졣
���ڶ�DPӦ�ó����ּ�����һЩ�˽⡣

###hot solution
```python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output
```
˼·�����������Ƕ�̬�滮�Ľⷨ��
���Ƚ���һ������б�
��ǰ���󣬰�ÿ��Ԫ��ǰ��Ĳ�����˻������ȥ��
֮�󵹹�������ÿ��Ԫ�غ�������ĳ˻��ٳ˽�ȥ��

###time consuming
#####hot solution
188ms