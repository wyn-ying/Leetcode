###idea
��Ŀ˵�����ź�������飬���˼·�Ƚ�������
�������뵽�ľ���˳���ң�ֱ��i>=target˵��target�������λ�ã������Ѿ����ˣ���Ҫ�������λ�á�

����û���ö��ֲ��ң���������һ�㡣

###hot solution
û�������أ��������Ƕ��ֲ��ҡ���������python��˳���ҺͶ����ҵĴ��롣
```python
# O(n) time 
def searchInsert1(self, nums, target):
    i = 0
    while i < len(nums):
        while i < len(nums) and nums[i] < target:
            i += 1
        return i

# O(lgn) time         
def searchInsert(self, nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        if l == r:
            if target <= nums[l]:
                return l
            else:
                return l+1
        mid = (l+r) >> 1
        if nums[mid] > target:
            r = mid 
        elif nums[mid] < target:
            l = mid + 1 
        else:
            return mid
```

###time consuming
#####my solution
40ms-->73.15%
#####hot solution1
52ms-->14.33%
#####hot solution2
48ms-->27.18%
����˼�ĵط�����Ologn���㷨��Ȼ��û�ҵ�On�Ŀ졣
����һ������������豸�йأ�һ����������ģ�йء�
�����ģС���ö��ֲ���׬�ı��˿��ܻ�������ֱȽϸ�ֵ���㣬�����Ƕ�python�����Ƚϸ߼������ԡ�