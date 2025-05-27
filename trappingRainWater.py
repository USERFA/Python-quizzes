from typing import List


def trap( height: List[int]) -> int:
    trapQuantity = 0
    for i in range(len(height)):
        maxLeft=max(height[:i+1])
        maxright=max(height[i:])
        trapQuantity += min(maxLeft,maxright)-height[i]

    return trapQuantity

    # maxLeft=0
    # maxright=0
    # for i in range(len(height)):
    #     for j in range(i+1,len(height)):
    #         if height[i]>maxLeft:
    #             maxLeft=height[i]
    #         if height[j]>maxright:
    #             maxright=height[j]
    #     trapQuantity += min(maxLeft,maxright)-height[i] 

    # return trapQuantity
        

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))