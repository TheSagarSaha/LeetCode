# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        print(arr)
        i = len(arr) - 1
        ans2 = ListNode()
        ans = ans2
        while i >= 0:
            node = ListNode(arr[i])
            ans.next = node
            ans = ans.next
            i -= 1
        return ans2.next
            
