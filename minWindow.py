def minWindow(s: str, t: str) -> str:
    word = ""
    s = sorted(s)
    if len(t)<=2:
        word= ""
    for i in range(len(s)-len(t)+1):
        print("up",s[i:i+len(t)])
        if t in s[i:i+len(t)]:
            word= s[i:i+len(t)]
    return word

print(minWindow("OUZODYXA3ZV","XYZ"))