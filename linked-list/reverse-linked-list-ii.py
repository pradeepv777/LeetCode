# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        
        slow = dummy
        for _ in range(left- 1):
            slow = slow.next

        curr = slow.next
        prev = None

        # rev the list left -> right
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        slow.next.next = curr
        slow.next = prev

        return dummy.next

        