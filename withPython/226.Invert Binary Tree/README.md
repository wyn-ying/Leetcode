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
˼·���ƣ�����ͨ���ݹ齻����������������ʵ�֡���ȻHot solution�������࣬����ִ��Ч�ʽϵͣ�Ӧ�������ˡ�,���������Ե�ʡ�

###time comsuming
######my solution
36ms
######hot solution
48ms