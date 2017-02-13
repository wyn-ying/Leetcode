###idea
开始没有想出来简单的做法，想过用深度优先搜索和递归，但好像比较麻烦，没想清楚。
看了一眼hot solution发现自己没有注意到是BST（二叉搜索树）。

思路：利用BST性质，对于距离p和q最近的共同祖先（根），那它们的与根的值之差必定异号。
因此遍历一遍树，发现满足条件的节点返回即可。

###hot solution
思路：在my idea的基础上又进了一步，既然是BST，判断p的value和当前root的value即可知道后面该往左走还是往右走。
```python
def lowestCommonAncestor(self, root, p, q):
    while (root.val - p.val) * (root.val - q.val) > 0:
        root = (root.left, root.right)[p.val > root.val]	#python中(x,y)[expression]类似：？运算符,True为y，False为x
    return root
```
然而感觉效率并不高，有时间再自己写一个或看看其他hot solution

###time consuming
#####hot solution
140ms