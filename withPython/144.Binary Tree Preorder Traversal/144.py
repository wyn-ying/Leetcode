class Solution(object):
    def preorderTraversal(self, root):
        ret = []
        stack = [root]
        while stack:
            tmp_node = stack.pop()
            if tmp_node is not None:
                ret.append(tmp_node.val)
                stack.append(tmp_node.right)
                stack.append(tmp_node.left)
        
        return ret