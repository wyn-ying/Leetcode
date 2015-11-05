class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        else:
            tmp = self.invertTree(root.left)
            root.left = self.invertTree(root.right)
            root.right = tmp
        return root        
