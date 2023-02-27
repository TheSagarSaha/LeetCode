# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        s = set()
        res = ListNode()
        node = res

        while head:
            if head.val not in s:
                curr = ListNode(head.val)
                node.next = curr
                node = node.next

            s.add(head.val)
            head = head.next
        return res.next
        
