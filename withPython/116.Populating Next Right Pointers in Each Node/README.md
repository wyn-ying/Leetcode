###idea
层序遍历（BFS）这个树（FIFO队列），满足2^n - 1条件的是每层最右节点，让其指向NULL，
其他的都指向后一个节点（即该节点被弹出后，指针指向队列最前面的节点）。
直到弹出的值是空为止。

判断最右的条件cnt + 1 == 2 ** n还有改进空间。

另外while循环显得无用，因为空指针也会被加入队列，使得len(d)永远大于0。
其实应该是tmp is None条件控制循环退出。这个地方刚也有改进空间。

最后猜测import地方也有耗时。

#####idea update
把判断root是否为空放到import前面，前面提到的两个地方做了优化，效率提高了不少。

###hot solution
python版的代码应该是根据hotest solution（C版本）的改进版本移植过来的。贴上主要用于对比时间效率。确实很快。
```python
def connect(self, root):
    if not root: return
    while root.left:
        cur = root.left
        prev = None
        while root:
            if prev: prev.next = root.left
            root.left.next = root.right
            prev = root.right
            root = root.next
        root = cur
```

#####hotest solution
没有用到BFS，非递归，挺巧妙的想法。
最里层循环中依次修改cur的左右子节点的next指针，让它们指向它们右边的节点，并依次向右移动cur，直到这一层所有节点的子节点都处理完。
pre节点用于记录树的层次并向下移动。
```c
void connect(TreeLinkNode *root) {
    if (root == NULL) return;
    TreeLinkNode *pre = root;
    TreeLinkNode *cur = NULL;
    while(pre->left) {
        cur = pre;
        while(cur) {
            cur->left->next = cur->right;
            if(cur->next) cur->right->next = cur->next->left;
            cur = cur->next;
        }
        pre = pre->left;
    }
}
```
这里再偷一点的话可以再省一个pointer，因为没有要求返回，直接用root代替pre的角色即可。[链接](https://leetcode.com/discuss/26868/my-simple-non-iterative-c-code-with-o-1-memory)

#####other code
java版本，采用了递归，空间复杂度大概O(logN)，不过比较优雅。
```Java
public void connect(TreeLinkNode root) {
    if(root == null)
        return;

    if(root.left != null){
        root.left.next = root.right;
        if(root.next != null)
            root.right.next = root.next.left;
    }

    connect(root.left);
    connect(root.right);
}
```
###time consuming
#####my solution
108ms-->21.96%
#####update solution
92ms-->62.4%
#####hot solution
88ms-->77.48%