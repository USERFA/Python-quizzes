def dailyTemperatures(temperatures: List[int]) -> List[int]:
        output=[]
        for i in range(len(temperatures)):
            print(i)
            for j in range(i+1,len(temperatures)):
                print('j',j)
                if temperatures[j]>temperatures[i]:
                    output.append(j-i)
                    break
            else:# j==len(temperatures)-1:
            # if temperatures[j]<=temperatures[i]:
                print('uuuu',temperatures[j])
                output.append(0)
        return output
    
#     for j in range(...):
#     if condition:
#         break
# else:
    # Runs only if the loop did not break
