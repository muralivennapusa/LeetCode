# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f,s=head,head
        h=head
        while f.next is not None and f is not None:
            s=s.next
            f=f.next.next
            if s==f:
                return True
        return False
