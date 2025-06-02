def lengthOfLongestSubstring(s: str) -> int:
    longestLength = 0
    seen = set() #will store substring without duplicates
    leftIndex=0
    for i in range(len(s)):
        while s[i] in seen: #true if there are duplicates
            seen.remove(s[leftIndex]) 
            leftIndex += 1 #shrink left side
        seen.add(s[i]) #add it to seen because there are no duplicates
        longestLength = max(longestLength, i-leftIndex+1)

    return longestLength



print(lengthOfLongestSubstring("zxyzxyz"))
print(lengthOfLongestSubstring("xxxx"))
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("pwwkew"))