def isPalindrome(s: str) -> bool:
    isPalindromeWord = False
    cleaned = ''.join(ch for ch in s if ch.isalnum()).lower()
    if(len(cleaned)<=1):
        return True
    for i in range(len(cleaned)):
            if(cleaned[i] == cleaned[len(cleaned)-i-1]):
                isPalindromeWord = True
            else:
                return False

    return isPalindromeWord





print(isPalindrome("Was it a car or a cat I saw?"))
print(isPalindrome("tab a cat"))
print(isPalindrome(".,"))
