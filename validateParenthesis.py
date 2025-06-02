def isValid(s: str) -> bool:
    hashMap = {"(": ")", "[": "]", "{": "}"}
    stack = []
    # s[l] == '(', it pushes ')' to the stack.
    for l in range(len(s)):
        if s[l] in hashMap:  # if it's an opening bracket
            stack.append(
                hashMap[s[l]]
            )  # append to the stack the closing tag of the opening tag
            print("stack", stack, "hashMap[s[l]]", hashMap[s[l]])
        elif (
            len(stack) == 0 or s[l] != stack.pop()
        ):  # runs if s[l] is a closing bracket
            return False
    return len(stack) == 0

 # while '()' in s or '{}' in s or '[]' in s:
            # s = s.replace('()', '')
            # s = s.replace('{}', '')
            # s = s.replace('[]', '')
        # return s == ''


print(isValid("([{}])"))
print(isValid("()[]{}"))
