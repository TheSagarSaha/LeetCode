# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter, length = 0, 0
        res = ListNode()
        ans = res
        head2 = head
        while head:
            length += 1
            head = head.next
        
        while head2:
            if counter != length-n:
                node = ListNode(head2.val)
                ans.next = node
                ans = ans.next
            counter += 1
            head2 = head2.next
        
        return res.next
