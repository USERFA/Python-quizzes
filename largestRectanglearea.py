from typing import List


def largestRectangleArea( heights: List[int]) -> int:
    # get the min height -> get the width -> get the area => get the max area
    maxArea=0

    for i in range(len(heights)):
        minHeight=heights[i]
        for j in range(i,len(heights)):
            minHeight=min(minHeight, heights[j])
            width = j-i+1
            area = minHeight*width
            maxArea= max(maxArea,area)
    
    return maxArea        