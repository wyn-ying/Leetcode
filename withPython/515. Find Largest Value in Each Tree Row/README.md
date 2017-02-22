###idea
用了一种最没创意的办法：使用队列的BFS。每次入队列的包括节点以及它所在的层数。出队列时比较层数，若在同一层就比较大小，若新出队的层数比现在保存的层数高，则把当前max（上一层的最大值）记录下来，并更新现在的层高和max。算法执行效率很低。应该是import Queue的缘故。
###solutions
都是用BFS，不过热答里的python代码没有用Queue，而是每次对一层进行操作。具体如下：
```python
def largestValues(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    maxes = []
    row = [root]
    while any(row):
        maxes.append(max(node.val for node in row))
        row = [kid for node in row for kid in (node.left, node.right) if kid]
    return maxes
```
这个代码的速度仍然不快，估计是反复改写row列表的缘故。不过已经比自己的快了。
###time consuming
#####my solution
162ms-->beats 4.44%
#####discuss solution
102ms-->beats 31.58%