from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    output=  []
    for l in range(len(nums)):
        subarray = nums[l:l+k] #array of lenght k
        output.append(max(subarray))
        if l+k == len(nums): #lenght of last array should be k
            break
        l+=1
    return output

print(maxSlidingWindow([1,2,1,0,4,2,6],3))
         
