from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    sortedNums=sorted(nums)
    output = []
    for i in range(len(sortedNums)):
        if i>0 and sortedNums[i] == sortedNums[i-1]:
            continue
        l,r = i+1 , len(sortedNums)-1
        while l<r:
            if sortedNums[l]+sortedNums[r]+sortedNums[i]>0:
                r-=1
            elif sortedNums[l]+sortedNums[r]+sortedNums[i]<0:
                l+=1
            else:
                output.append([sortedNums[l],sortedNums[r],sortedNums[i]])
                while l<r and sortedNums[l]==sortedNums[l+1]:
                    l+=1
                while l<r and sortedNums[r]==sortedNums[r-1]:
                    r-=1
                r-=1
                l+=1
    return output

# print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([-2,0,0,2,2]))

        
