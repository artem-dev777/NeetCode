# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Despite being marked as a hard problem the solution is actually fairly straightforward.
# From previous easy task we already know how to revers a linked list, so we just reuse that algorithm here.
# The trick is to not reverse the entire list, but reverse each segment of k elements.
# So we just count k elements  from head, reverse them
# and then reattach new (reversed) head and new (reversed) tail to the main list.
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
                # head of the current segment of k elements will become tail
                rev_tail = prev_tail.next
                rev_head = self.reverseList(prev_tail.next)

                # now reattach the reversed segment to the main list
                prev_tail.next = rev_head
                prev_tail = rev_tail
                
                curr = rev_tail
                curr.next = tmp_next
            
            curr = curr.next
        return dummy.next
