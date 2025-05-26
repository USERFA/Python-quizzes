from typing import List

def longestConsecutive(nums: List[int]) -> int:
    consecutive=1
    longest=1
    numSet=sorted(set(nums))
    if len(numSet)==0:
         return 0
    for i in range(len(numSet)-1):
            if numSet[i+1]-numSet[i] == 1:
                consecutive+=1
                longest = max(longest, consecutive)
                # print(longest)
            else:
                 consecutive=1
            # else:
            #     break

    return longest

# print(longestConsecutive([100,4,200,1,3,2]))
# print(longestConsecutive([0,3,2,5,4,6,1,1]))
# print(longestConsecutive([2,20,4,10,3,4,5]))
# print(longestConsecutive([]))
print(longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))