from typing import Optional

from reverseList import ListNode, buildLinkedList

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    prev = dummy
    currentList1 = list1
    currentList2 = list2
    while currentList1 and currentList2:
        if currentList1.val > currentList2.val:
            prev.next = currentList2
            currentList2 = currentList2.next 
        else:
            prev.next = currentList1
            currentList1 = currentList1.next
        prev = prev.next
        
    if currentList1:
        prev.next = currentList1
    if currentList2:
        prev.next = currentList2
    
    while(currentList1):
        print('currentList1.val',currentList1.val)
    return dummy.next #first node of the merged list

print(mergeTwoLists(buildLinkedList([1,2,4]),buildLinkedList([1,3,4])))
