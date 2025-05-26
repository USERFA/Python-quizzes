from typing import List


def topKFrequent( nums: List[int], k: int) -> List[int]:
    freq={}
    for i in range(len(nums)):
        if nums[i] in freq:
            freq[nums[i]]+=1
        else:
            freq[nums[i]]=1
    sortedFreq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in sortedFreq[:k]]

    # return dict

print(topKFrequent([1,3,3,2,2,3],2))
