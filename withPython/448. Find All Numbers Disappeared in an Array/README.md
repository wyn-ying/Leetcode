###idea
Ҫ��ʹ�ö���ռ䣬��������ʱ��õ������û��ʲô��˼·������д��һ��pythonic�Ĵ��롣

˼·��ֱ����set��difference�����������set(range)��set(nums)�Ĳ��

###hot solution
ͨ����ÿ������Ϊ��Ŷ�Ӧ���Ǹ����ĳɸ�����O(n)ʱ����԰�listɨ��һ�飬��list�д��ڵ�����������Ϊ�±���list�е��������ĳ��˸�������ôlist���������Ķ�Ӧ��������miss�ġ�

������������������±������������ǡ������ٶ�ƫ����
```python
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        idx=0
        for i in xrange(len(nums)):
            idx=abs(nums[i])-1
            nums[idx] = -abs(nums[idx])
        return [i+1 for i in range(len(nums)) if nums[i]>0]
```
###time consuming
#####my solution
272ms-->beats 90.14%
#####hot solution
349ms-->beats 53.56%