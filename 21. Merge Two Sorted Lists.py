# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

            head = ListNode()
            cur = head
            while list1 and list2:

                l1 = list1.val
                l2 = list2.val

                if l1 > l2:
                    cur.next = ListNode(l2, None)
                    cur = cur.next
                    list2 = list2.next
                else:
                    cur.next = ListNode(l1, None)
                    cur = cur.next
                    list1 = list1.next


            while list1:
                cur.next = ListNode(list1.val, None)
                cur = cur.next
                list1 = list1.next

            while list2:
                cur.next = ListNode(list2.val, None)
                cur = cur.next
                list2 = list2.next

            return head.next
