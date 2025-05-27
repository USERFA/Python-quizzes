from typing import List


def maxArea(heights: List[int]) -> int:
    area=1
    maxArea=1
    for i in range(len(heights)):
        for j in range(i+1,len(heights)):
            if i==j:
                continue
            area=min(heights[i],heights[j])*(j-i)
            maxArea=max(maxArea,area)

    return maxArea

print(maxArea([1,7,2,5,4,7,3,6]))
print(maxArea([2,2,2]))