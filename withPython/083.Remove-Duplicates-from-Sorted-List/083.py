class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = head
        while head != None and head.next != None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
                
        return h
