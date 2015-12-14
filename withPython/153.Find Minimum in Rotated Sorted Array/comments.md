###idea
把数组看一遍，比前一项小的都有可能是最小项，把它和已经记录的最小项比较，最后找到整个数组中最小的那个。

###hot solution
[最高票](https://leetcode.com/discuss/13389/compact-and-clean-c-solution)是C++版本，二分查找的思路。
因为数组是有序的，每次比较首和尾，如果首比尾大，必然存在rotate；如果尾比首大，则不存在rotate。这里仿佛利用了只有一个pivot……
之后找首比尾大的那一半继续搜索，直到缩成一项。时间效率是On的。
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
python版本：
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
实测也没有想象中差距大，可能是n较小的缘故。
