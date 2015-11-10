###idea
最普通的运用递归的中序遍历算法，注意根据要求操作好返回的列表即可，nothing special。

###hot solution
看了很多hot solution，发现它们都用了堆栈和循环而没有使用递归，这应当是个不错的思路。
使用栈的算法大同小异，相比之下python代码显得简洁优美：
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