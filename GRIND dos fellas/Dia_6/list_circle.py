from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        list_id = set()
        while(head != None):
            if(id(head) not in list_id):
                list_id.add(id(head))
                head = head.next
            else:
                return True
        return False