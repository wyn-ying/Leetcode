# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        sum, d = self.dfs(root)
        most_freq = max(d.values())
        r=[]
        for k,v in d.items():
            if v == most_freq:
                r.append(k)
        return r
    def dfs(self, node):
        suml = 0
        sumr = 0
        dl={}
        dr={}
        if node.left is not None:
            suml, dl = self.dfs(node.left)
        if node.right is not None:
            sumr, dr = self.dfs(node.right)
        d = self.combine(dl, dr)
        s = suml+sumr+node.val
        d[s] = d.get(s, 0) + 1
        return s, d
    def combine(self, d1, d2):
        for k, v in d2.items():
            d1[k] = d1.get(k, 0)+v
        return d1 if len(d1)>0 else {}