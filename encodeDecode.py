from typing import List


def encode(strs: List[str]) -> str:
    encodedStr=""
    for s in strs:
        print(s)
        encodedStr+=str(len(s))+"#,"+s
    return encodedStr

print(encode(["Hello","World","again!"]))



    
def decode(s: str) -> List[str]:
    decodedList = []
    i = 0
    while i < len(s):
        length_str = ""
        while i < len(s) and s[i].isdigit():
            # digit =length
            length_str += s[i]
            i += 1
        i += 2  # skip '#'
        length = int(length_str)
        print(length_str)
        substring = s[i:i+length]
        decodedList.append(substring)
        i += length  
    return decodedList
    # decodedList=[]
    # length=[]
    # for i in range(len(s)):
    #     # print(s[i])
    #     if(s[i].isdigit()):
    #         length.append(s[i])
    # for i in range(len(s)):
    #     for j in range(len(length)):
    #         if(s[i]=="#"):
    #             if(s[i+1]==","):
    #                 decodedList.append(s[i+2:int(length[i])])
    # return decodedList

print(decode("5#,Hello5#,World6#,again!"))