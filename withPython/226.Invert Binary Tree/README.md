###hot solution
```python
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root  
```
思路类似，都是通过递归交换左子树和右子树实现。显然Hot solution代码更简洁，但是执行效率较低，应该是用了‘,’运算符的缘故。

###time comsuming
######my solution
36ms
######hot solution
48ms