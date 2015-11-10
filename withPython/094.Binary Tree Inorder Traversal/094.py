class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lst = []
        if root is None:
            return []
        else:
            lst_left = self.inorderTraversal(root.left)
            for i in lst_left:
                lst.append(i)
                
            lst.append(root.val)
            lst_right = self.inorderTraversal(root.right)
            for i in lst_right:
                lst.append(i)
        
        return lst