###idea
����һ����û����İ취��ʹ�ö��е�BFS��ÿ������еİ����ڵ��Լ������ڵĲ�����������ʱ�Ƚϲ���������ͬһ��ͱȽϴ�С�����³��ӵĲ��������ڱ���Ĳ����ߣ���ѵ�ǰmax����һ������ֵ����¼���������������ڵĲ�ߺ�max���㷨ִ��Ч�ʺܵ͡�Ӧ����import Queue��Ե�ʡ�
###solutions
������BFS�������ȴ����python����û����Queue������ÿ�ζ�һ����в������������£�
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
���������ٶ���Ȼ���죬�����Ƿ�����дrow�б��Ե�ʡ������Ѿ����Լ��Ŀ��ˡ�
###time consuming
#####my solution
162ms-->beats 4.44%
#####discuss solution
102ms-->beats 31.58%