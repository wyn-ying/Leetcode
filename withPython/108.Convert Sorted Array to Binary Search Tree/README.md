###idea
数组转成二叉搜索树（BST），最简单的想法就是每次把中间的数放在root，之后递归左右两段，分别放在左子树和右子树。当然这样的做法时间效率很低。

###hot solution
hot solution里也没有什么新奇特，[高票中的python答案](https://leetcode.com/discuss/28867/an-easy-python-solution)思路差不多。
```python
class Solution:
    # @param num, a list of integers
    # @return a tree node
    # 12:37
    def sortedArrayToBST(self, num):
        if not num:
            return None

        mid = len(num) // 2

        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])

        return root
```

###time comsuming
#####my solution
124ms-->3.94%
#####hot solution
96ms-->70.25%