# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        duplicate = set()
        nums = []

        while head:
            if head.val in nums:
                duplicate.add(head.val)
            nums.append(head.val)
            head = head.next

        res = ListNode()
        node = res

        for i in nums:
            if i not in duplicate:
                curr = ListNode(i)
                node.next = curr
                node = node.next
        
        return res.next
        
