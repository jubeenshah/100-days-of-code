class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = newNode = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                newNode.next = l1
                l1 = l1.next
            else:
                newNode.next = l2
                l2 = l2.next
            newNode = newNode.next
        newNode.next = l1 or l2
        return dummy.next