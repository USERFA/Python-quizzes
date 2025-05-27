def checkInclusion(s1: str, s2: str) -> bool:
    s1 = sorted(s1)
    lenS1 = len(s1)
    # s2 = sorted(s2)
    for i in range(len(s2)-lenS1+1):
        print(sorted(s2[i:i+lenS1])) 
        if sorted(s2[i:i+lenS1]) == s1:
            return True 
    return False
        
# print(checkInclusion("abc","lecabee"))
# print(checkInclusion("abc","lecaabee"))
print(checkInclusion("ab","eidboaoo"))
        