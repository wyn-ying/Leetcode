###idea
��ʼû��������򵥵������������������������͵ݹ飬������Ƚ��鷳��û�������
����һ��hot solution�����Լ�û��ע�⵽��BST����������������

˼·������BST���ʣ����ھ���p��q����Ĺ�ͬ���ȣ������������ǵ������ֵ֮��ض���š�
��˱���һ�������������������Ľڵ㷵�ؼ��ɡ�

###hot solution
˼·����my idea�Ļ������ֽ���һ������Ȼ��BST���ж�p��value�͵�ǰroot��value����֪������������߻��������ߡ�
```python
def lowestCommonAncestor(self, root, p, q):
    while (root.val - p.val) * (root.val - q.val) > 0:
        root = (root.left, root.right)[p.val > root.val]	#python��(x,y)[expression]���ƣ��������,TrueΪy��FalseΪx
    return root
```
Ȼ���о�Ч�ʲ����ߣ���ʱ�����Լ�дһ���򿴿�����hot solution

###time consuming
#####hot solution
140ms