###idea
����ͨ�����õݹ����������㷨��ע�����Ҫ������÷��ص��б��ɣ�nothing special��

###hot solution
���˺ܶ�hot solution���������Ƕ����˶�ջ��ѭ����û��ʹ�õݹ飬��Ӧ���Ǹ������˼·��
ʹ��ջ���㷨��ͬС�죬���֮��python�����Եü��������
```python
def inorderTraversal(self, root):
    ans = []
    stack = []

    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            tmpNode = stack.pop()
            ans.append(tmpNode.val)
            root = tmpNode.right

    return ans
```

###time consuming
#####my solution
40ms
#####hot solution
48ms