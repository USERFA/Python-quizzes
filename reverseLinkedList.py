# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

def buildLinkedList(nums):
    dummy = ListNode()
    current = dummy
    for num in nums:
        # We create a new node ListNode(num) with that number+ we link it to the current node by assigning it to current.next.
        current.next = ListNode(num)
        current = current.next
    return dummy.next   #head of the list


def reverseList( head: Optional[ListNode]) -> Optional[ListNode]:
    prev=None
    current= head
    print(current)
    while current:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode
    return prev



print(reverseList(buildLinkedList([1,2,3,4,5])))