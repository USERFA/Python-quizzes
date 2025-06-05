from typing import Optional

from reverseList import ListNode, buildLinkedList


def hasCycle(head: Optional[ListNode]) -> bool:
    # Floyds cycle
    current = head
    currentAhead = head
    while current and currentAhead and currentAhead.next:
        current = current.next
        currentAhead= currentAhead.next.next
        if current == currentAhead:
            return True
    return False
        # if current.next == prev:
            # return True
        # prev = current
        # current = current.next  
    # return False


print(hasCycle(buildLinkedList([1,2,3,4,5])))