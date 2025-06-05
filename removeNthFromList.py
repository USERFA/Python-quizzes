from typing import Optional

from reverseList import ListNode, buildLinkedList


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    if n == length:
        return head.next

    current = head
    position = 1
    while current:
        if position == length - n:
            current.next = current.next.next
            break
        current = current.next
        position += 1

    return head
    

print(removeNthFromEnd(buildLinkedList([1,2,3,4,5]),2))
        