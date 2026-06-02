# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # merged = None
        # mergedCurrent = None

        # while list1 and list2:
        #     if list1.val <= list2.val:
        #         if merged and mergedCurrent:
        #             mergedCurrent.next = ListNode(list1.val)
        #             mergedCurrent = mergedCurrent.next
        #         else:
        #             merged = ListNode(list1.val)
        #             mergedCurrent = merged

        #         list1 = list1.next
        #     else:
        #         if merged and mergedCurrent:
        #             mergedCurrent.next = ListNode(list2.val)
        #             mergedCurrent = mergedCurrent.next
        #         else:
        #             merged = ListNode(list2.val)
        #             mergedCurrent = merged

        #         list2 = list2.next

        # while list1:
        #     if merged and mergedCurrent:
        #         mergedCurrent.next = ListNode(list1.val)
        #         mergedCurrent = mergedCurrent.next
        #     else:
        #         merged = ListNode(list1.val)
        #         mergedCurrent = merged
            
        #     list1 = list1.next

        # while list2:
        #     if merged and mergedCurrent:
        #         mergedCurrent.next = ListNode(list2.val)
        #         mergedCurrent = mergedCurrent.next
        #     else:
        #         merged = ListNode(list2.val)
        #         mergedCurrent = merged
            
        #     list2 = list2.next

        # Using an empty "dummy" node to start, makes the code cleaner and prevents always having to check if the first node exists or not
        merged = ListNode()
        mergedCurrent = merged

        while list1 and list2:
            if list1.val <= list2.val:
                mergedCurrent.next = ListNode(list1.val)
                list1 = list1.next
            else:
                mergedCurrent.next = ListNode(list2.val)
                list2 = list2.next

            mergedCurrent = mergedCurrent.next

        while list1:
            mergedCurrent.next = ListNode(list1.val)
            
            mergedCurrent = mergedCurrent.next
            list1 = list1.next

        while list2:
            mergedCurrent.next = ListNode(list2.val)
            
            mergedCurrent = mergedCurrent.next
            list2 = list2.next

        return merged.next