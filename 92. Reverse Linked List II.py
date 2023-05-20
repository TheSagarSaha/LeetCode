# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        revList = []
        leftList = []
        rightList = []
        i = 1
        while head:
            if i < left:
                leftList.append(head.val)
            elif i >= left and i <= right:
                revList.append(head.val)
            else:
                rightList.append(head.val)
            head = head.next
            i += 1

        linkedList = leftList + revList[::-1] + rightList
        res = ListNode()
        res2 = res

        for i in linkedList:
            node = ListNode(i)
            res2.next = node
            res2 = res2.next

        return res.next
