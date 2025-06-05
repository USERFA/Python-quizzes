from typing import Optional

from reverseList import ListNode, buildLinkedList


def reorderList( head: Optional[ListNode]) -> None:
    dummy = ListNode()
    prev = dummy
    current = head
    data = []
    finaldata=[]
    while current:
        data.append(current.val)
        current = current.next
    # print(data)

    left = 0
    right = len(data)-1
    while left<=right:
        # mid = (left+right)//2
        if left == right:
            finaldata.append(data[left])
        else:
            finaldata.append(data[left])
            finaldata.append(data[right])
        left+=1
        right-=1
    
    current = head
    i=0
    while current:
        current.val = finaldata[i]
        current = current.next
        i+=1
        # print(buildLinkedList(finaldata))
    # print('final data',finaldata)

    # return buildLinkedList(finaldata)




print(reorderList(buildLinkedList([1,2,3,4,5])))