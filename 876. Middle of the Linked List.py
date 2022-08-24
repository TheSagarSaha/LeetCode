# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head2 = head
        count = 0
        while True:
            if head:
                count += 1
            else:
                break;
            head = head.next
        
        if count % 2 == 0:
            count = count // 2 
        else:
            count = count // 2
        
        
        count2 = 0
        while count2 != count:
            count2 += 1
            head2 = head2.next
        
        return head2
            
