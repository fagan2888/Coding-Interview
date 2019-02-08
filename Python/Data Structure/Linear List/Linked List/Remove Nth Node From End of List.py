# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        self.next = head
        p1, p2 = head, self
        for _ in range(n):
            p1 = p1.next
        while p1:
            p1, p2 = p1.next, p2.next
        p2.next = p2.next.next
        return self.next
        