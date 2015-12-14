###idea
�����鿴һ�飬��ǰһ��С�Ķ��п�������С��������Ѿ���¼����С��Ƚϣ�����ҵ�������������С���Ǹ���

###hot solution
[���Ʊ](https://leetcode.com/discuss/13389/compact-and-clean-c-solution)��C++�汾�����ֲ��ҵ�˼·��
��Ϊ����������ģ�ÿ�αȽ��׺�β������ױ�β�󣬱�Ȼ����rotate�����β���״��򲻴���rotate������·�������ֻ��һ��pivot����
֮�����ױ�β�����һ�����������ֱ������һ�ʱ��Ч����On�ġ�
```c++
int findMin(vector<int> &num) {
    int start=0,end=num.size()-1;

    while (start<end) {
        if (num[start]<num[end])
            return num[start];

        int mid = (start+end)/2;

        if (num[mid]>=num[start]) {
            start = mid+1;
        } else {
            end = mid;
        }
    }
    return num[start];
}
```
python�汾��
```python
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        while i < j:
            m = i + (j - i) / 2
            if nums[m] > nums[j]:
                i = m + 1
            else:
                j = m
        return nums[i]
```

###time consuming
#####my solution
48ms-->22.91%
#####hot solution
44ms-->46.48%
ʵ��Ҳû�������в��󣬿�����n��С��Ե�ʡ�
