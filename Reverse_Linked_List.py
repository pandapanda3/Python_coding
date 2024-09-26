from typing import Optional
# # leetcode 75: 206. Reverse Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = pre
            pre = current
            current = next_node
        return pre