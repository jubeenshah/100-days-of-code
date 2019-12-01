# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLength(self, head: ListNode) -> int:
        length = 0
        temp = head
        if not temp:
            return 0
        while temp.next:
            length += 1
            temp = temp.next
        return length+1
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return None
        dummy = ListNode(-1)
        dummy.next = head
        s, e = dummy, None
        def helper(node):
            nonlocal s,e
            if not node: return 0
            index = helper(node.next)+1
            if index == n+1: s = node
            if index == n-1: e = node            
            return index     
        helper(head)
        s.next = e
        return dummy.next