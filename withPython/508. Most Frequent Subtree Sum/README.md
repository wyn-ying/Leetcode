###idea
���˳���˼·��DFS�����������������ص�ǰ�ڵ��sum�����ṩ�����ڵ���sum��ͬʱ���ص�ǰ�ڵ���۵����е�sumֵ��key���ʹ�����value�����ɵ��ֵ䡣ÿ���ڵ���������������ֵ���Ϣ�������ڵ��ҵ����Ĵ�����ת��Ϊlist�����
###solutions
�ȴ�Ĵ���˼·���ƣ�����û����dict������������ȫ�ֵ�counter�����������ֵҲ�����Լ�д�ļ�����
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
Ч�ʲ�ࡣ
###time consuming
#####my solution
122ms-->beats 21.94%
#####discuss solution
99ms-->beats 51.44%