# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nextNode = curr.next

            # Reverse current node's next pointer
            curr.next = prev

            # Move pointers one position ahead
            prev = curr
            curr = nextNode

        return prev