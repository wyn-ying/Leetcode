# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        stack = []
        while head != None:
            stack.append(head)
            head = head.next
        head = stack.pop()
        r = head
        while len(stack) > 0:
            r.next = stack.pop()
            r = r.next
        
        r.next = None
        return head