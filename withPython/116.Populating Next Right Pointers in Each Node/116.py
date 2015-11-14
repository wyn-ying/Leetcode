# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        from collections import deque
        d = deque()
        d.append(root)
        n = 1
        cnt = 0
        while len(d) > 0:
            tmp = d.popleft()
            if tmp is None:
                return
            cnt += 1
            d.append(tmp.left)
            d.append(tmp.right)
            if cnt + 1 == 2 ** n:
                tmp.next = None
                n += 1
            else:
                tmp.next = d[0]
#update $ optimize
class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root is None:
            return
        d = collections.deque()
        d.append(root)
        n = 2
        cnt = 1
        while len(d) > 0:
            tmp = d.popleft()
            cnt += 1
            if tmp.left:
                d.append(tmp.left)
                d.append(tmp.right)
            if cnt == n:
                tmp.next = None
                n = n * 2
            else:
                tmp.next = d[0]