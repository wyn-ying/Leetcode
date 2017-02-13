###idea
题目说了是排好序的数组，因此思路比较清晰。
最容易想到的就是顺序找，直到i>=target说明target就在这个位置，或者已经过了，需要插在这个位置。

这里没有用二分查找，或许会更快一点。

###hot solution
没有新奇特，基本都是二分查找。这里贴了python版顺序找和二分找的代码。
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
有意思的地方在于Ologn的算法居然还没我的On的快。
猜想一方面跟服务器设备有关，一方面跟输入规模有关。
输入规模小的用二分查找赚的便宜可能还不如各种比较赋值划算，尤其是对python这样比较高级的语言。