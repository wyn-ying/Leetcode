# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        r=[]
        import Queue
        q=Queue.Queue()
        q.put((root,1))
        height=1
        max=root.val
        while not q.empty():
            node, h = q.get()
            if node.left is not None:
                q.put((node.left, h+1))
            if node.right is not None:
                q.put((node.right, h+1))
            if h>height:
                r.append(max)
                height += 1
                max=node.val
            else:
                if max<node.val:
                    max=node.val
        r.append(max)
        return r