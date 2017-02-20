# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        height=1
        r=root.val
        height, val = self.Dfs(root, height)
        return val
    def Dfs(self, root, height):
        if root is None:
            return 0, None
        else:
            lh, lval = self.Dfs(root.left, height)
            lh += 1
            rh, rval = self.Dfs(root.right, height)
            rh += 1
            if lval is None and rval is None:
                return 1, root.val
            else:
                return (lh, lval) if lh >= rh else (rh, rval)