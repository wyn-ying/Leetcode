class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        h = ListNode(-1)
        h.next = head
        head = h
        while head != None and head.next != None:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
                
        return h.next
