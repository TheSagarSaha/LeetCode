# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        res = ListNode()
        node = res

        while head:
            if head.val != val:
                curr = ListNode(head.val)
                node.next = curr
                node = node.next
            head = head.next
        
        return res.next
