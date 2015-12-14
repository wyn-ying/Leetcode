# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 1:
            return TreeNode(nums[0])
        elif len(nums) == 0:
            return None
        else:
            mid = len(nums)/2
            r = TreeNode(nums[mid])
            r.left = self.sortedArrayToBST(nums[:mid])
            r.right = self.sortedArrayToBST(nums[mid+1:])
            return r
            