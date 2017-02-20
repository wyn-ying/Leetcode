###idea
简单的树遍历，检索树高并返回左右子树中较高的子树的最左边元素，若左右等高，返回左边的。
代码写的还是不很熟练，执行效率也较低。
###solutions
一个急速版的java代码，改写为python如下：
```python
class Solution(object):
    def __init__(self):
        self.h=0
        self.ans=0
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.Dfs(root, 1)
        return self.ans
    def Dfs(self, root, height):
        if self.h<height:
            self.ans = root.val
            self.h = height
        if root.left is not None:
            self.Dfs(root.left, height+1)
        if root.right is not None:
            self.Dfs(root.right, height+1)
```
思路很简单：因为DFS先遍历左子树，那么全局变量h会优先被左边较深的树更新。只要新的子树树高没有超过全局变量h，那么就不能更新ans。

除了DFS，BFS也是挺好的办法。思路：从右向左做一次BFS，最后输出的就是最底下一层最左边的节点。
```python
def findBottomLeftValue(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    queue = [root]
    for node in queue:
        queue += filter(None, (node.right, node.left))
    return node.val
```
###time consuming
#####my solution
109ms-->beats 14.21%
#####discuss solution
72ms-->beats 74.21%