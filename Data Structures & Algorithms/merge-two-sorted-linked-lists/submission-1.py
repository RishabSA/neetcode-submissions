# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = None
        mergedCurrent = None

        current1 = list1
        current2 = list2

        while current1 and current2:
            if current1.val <= current2.val:
                if merged and mergedCurrent:
                    mergedCurrent.next = ListNode(current1.val)
                    mergedCurrent = mergedCurrent.next
                else:
                    merged = ListNode(current1.val)
                    mergedCurrent = merged

                current1 = current1.next
            else:
                if merged and mergedCurrent:
                    mergedCurrent.next = ListNode(current2.val)
                    mergedCurrent = mergedCurrent.next
                else:
                    merged = ListNode(current2.val)
                    mergedCurrent = merged

                current2 = current2.next

        if current1:
            while current1:
                if merged and mergedCurrent:
                    mergedCurrent.next = ListNode(current1.val)
                    mergedCurrent = mergedCurrent.next
                else:
                    merged = ListNode(current1.val)
                    mergedCurrent = merged
                
                current1 = current1.next

        if current2:
            while current2:
                if merged and mergedCurrent:
                    mergedCurrent.next = ListNode(current2.val)
                    mergedCurrent = mergedCurrent.next
                else:
                    merged = ListNode(current2.val)
                    mergedCurrent = merged
                
                current2 = current2.next

        return merged