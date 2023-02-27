# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = ""
        list2 = ""
        
        while(l1):
            list1 += str((l1.val))
            l1 = l1.next
        
        while(l2):
            list2 += str((l2.val))
            l2 = l2.next
        
        ans = int(list1[::-1]) + int(list2[::-1])
        ans = str(ans)[::-1]
        
        node = ListNode()
        res = node
        for i in ans:
            node1 = ListNode(int(i))
            res.next = node1
            res = res.next
            
        return node.next
        
        
