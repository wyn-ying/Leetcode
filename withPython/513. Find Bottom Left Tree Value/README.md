###idea
�򵥵����������������߲��������������нϸߵ������������Ԫ�أ������ҵȸߣ�������ߵġ�
����д�Ļ��ǲ���������ִ��Ч��Ҳ�ϵ͡�
###solutions
һ�����ٰ��java���룬��дΪpython���£�
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
˼·�ܼ򵥣���ΪDFS�ȱ�������������ôȫ�ֱ���h�����ȱ���߽���������¡�ֻҪ�µ���������û�г���ȫ�ֱ���h����ô�Ͳ��ܸ���ans��

����DFS��BFSҲ��ͦ�õİ취��˼·������������һ��BFS���������ľ��������һ������ߵĽڵ㡣
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