###idea
����ת�ɶ�����������BST������򵥵��뷨����ÿ�ΰ��м��������root��֮��ݹ��������Σ��ֱ����������������������Ȼ����������ʱ��Ч�ʺܵ͡�

###hot solution
hot solution��Ҳû��ʲô�����أ�[��Ʊ�е�python��](https://leetcode.com/discuss/28867/an-easy-python-solution)˼·��ࡣ
```python
class Solution:
    # @param num, a list of integers
    # @return a tree node
    # 12:37
    def sortedArrayToBST(self, num):
        if not num:
            return None

        mid = len(num) // 2

        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])

        return root
```

###time comsuming
#####my solution
124ms-->3.94%
#####hot solution
96ms-->70.25%