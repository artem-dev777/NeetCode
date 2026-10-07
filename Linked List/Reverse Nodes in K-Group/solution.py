# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]):
        prev, curr = None, head

        while curr:
            future = curr.next
            curr.next = prev
            prev = curr
            curr = future
        
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        dummy = prev_tail = ListNode(next=head)
        count = 0

        while curr:
            count += 1
            if count % k == 0:
                count = 0
                
                tmp_next = curr.next
                curr.next = None
                rev_tail = prev_tail.next
                rev_head = self.reverseList(prev_tail.next)

                prev_tail.next = rev_head
                prev_tail = rev_tail
                
                curr = rev_tail
                curr.next = tmp_next
            
            curr = curr.next
        return dummy.next
