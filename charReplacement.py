from collections import defaultdict

def characterReplacement( s: str, k: int) -> int:
    # exapmle AAABAB , here you can replace twice B with A, but k =1 so we stop at the length where only one change is possible
    maxLength =0 #longest valid substring we’ve seen so far
    maxCount=0 # count of the most frequent character A ->4
    left =0
    dicto = defaultdict(int) #{'A': 2, 'B': 3}

    # (window size - max_count)

    for right in range(len(s)):
            dicto[s[right]] += 1 #fill the dictionary
            print("dict",dicto)
            maxCount = max(maxCount, dicto[s[right]])
            print("dicto[s[right]]",dicto[s[right]] , dicto[s[left]]) #right : count A , left : count B
            if right-left+1 - maxCount > k: #window size - max_count = numbers of characters that can be replaced
                dicto[s[left]] -= 1
                left += 1
            print("right",right,"left",left)

            maxLength = max(maxLength, right-left+1)

        # s.replace(char,)    
        # count+=1
    print("def dict",dicto)

    return maxLength

        




# print(characterReplacement("XYXY", 2)) #4
print(characterReplacement("AAABABB", 1)) 