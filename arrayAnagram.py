from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    dict = {}
    for i in range(len(strs)):
        sortedStr = ''.join(sorted(strs[i]))
        if sortedStr in dict:
            dict[sortedStr].append(strs[i])
        else:
            dict[sortedStr] = [strs[i]]
    return list(dict.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
        