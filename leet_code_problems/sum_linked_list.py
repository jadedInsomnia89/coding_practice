from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        list_pointer = new_list
        num = 0

        while l1 or l2:
            num = num // 10
            
            if l1:
                num += l1.val
                l1 = l1.next
                
            if l2:
                num += l2.val
                l2 = l2.next
                
            list_pointer.next = ListNode(num % 10)
            list_pointer = list_pointer.next
            
        if num // 10 == 1:
            list_pointer.next = ListNode(num // 10)

        return new_list.next
