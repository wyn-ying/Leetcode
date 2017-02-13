###idea
���������BFS���������FIFO���У�������2^n - 1��������ÿ�����ҽڵ㣬����ָ��NULL��
�����Ķ�ָ���һ���ڵ㣨���ýڵ㱻������ָ��ָ�������ǰ��Ľڵ㣩��
ֱ��������ֵ�ǿ�Ϊֹ��

�ж����ҵ�����cnt + 1 == 2 ** n���иĽ��ռ䡣

����whileѭ���Ե����ã���Ϊ��ָ��Ҳ�ᱻ������У�ʹ��len(d)��Զ����0��
��ʵӦ����tmp is None��������ѭ���˳�������ط���Ҳ�иĽ��ռ䡣

���²�import�ط�Ҳ�к�ʱ��

#####idea update
���ж�root�Ƿ�Ϊ�շŵ�importǰ�棬ǰ���ᵽ�������ط������Ż���Ч������˲��١�

###hot solution
python��Ĵ���Ӧ���Ǹ���hotest solution��C�汾���ĸĽ��汾��ֲ�����ġ�������Ҫ���ڶԱ�ʱ��Ч�ʡ�ȷʵ�ܿ졣
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
û���õ�BFS���ǵݹ飬ͦ������뷨��
�����ѭ���������޸�cur�������ӽڵ��nextָ�룬������ָ�������ұߵĽڵ㣬�����������ƶ�cur��ֱ����һ�����нڵ���ӽڵ㶼�����ꡣ
pre�ڵ����ڼ�¼���Ĳ�β������ƶ���
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
������͵һ��Ļ�������ʡһ��pointer����Ϊû��Ҫ�󷵻أ�ֱ����root����pre�Ľ�ɫ���ɡ�[����](https://leetcode.com/discuss/26868/my-simple-non-iterative-c-code-with-o-1-memory)

#####other code
java�汾�������˵ݹ飬�ռ临�Ӷȴ��O(logN)�������Ƚ����š�
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