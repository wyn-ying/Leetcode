###idea
用了常规思路：DFS后序遍历这个树，返回当前节点的sum用来提供给父节点算sum，同时返回当前节点积累的所有的sum值（key）和次数（value）构成的字典。每个节点汇总左右子树的字典信息。最后根节点找到最大的次数，转换为list输出。
###solutions
热答的代码思路类似，不过没有用dict计数而是用了全局的counter，最后输出最大值也比我自己写的简练：
```python
def findFrequentTreeSum(self, root):
    import collections
    ctr = collections.Counter()
    if root == None: return []
    self.countTreeSum(root, ctr)
    frequent = max(ctr.values())
    return [i for i in ctr.keys() if ctr[i] == frequent]

  def countTreeSum(self, root, ctr):
    if root == None: return 0
    else:
      val = self.countTreeSum(root.left, ctr) + self.countTreeSum(root.right, ctr) + root.val
      ctr[val] += 1
      return val
```
效率差不多。
###time consuming
#####my solution
122ms-->beats 21.94%
#####discuss solution
99ms-->beats 51.44%