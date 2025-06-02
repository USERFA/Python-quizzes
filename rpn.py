from typing import List


def evalRPN(tokens: List[str]) -> int:

    expr = ""
    numStack = []
    for i in range(len(tokens)):

        # if tokens[i].isdigit() or tokens[i].isnumeric():
        if tokens[i].lstrip('-').isdigit():
            numStack.append(tokens[i])
        else:
            num1 = numStack.pop()
            num2 = numStack.pop()
            #  in Reverse Polish Notation, when you pop two operands:
            # num2 is the first operand
            # num1 is the second operand
            if tokens[i] == '+':
                numStack.append(int(num2) + int(num1))
            elif tokens[i] == '-':
                numStack.append(int(num2) - int(num1))
            elif tokens[i] == '*':
                numStack.append(int(num2) * int(num1))
            elif tokens[i] == '/':
                numStack.append(int(num2) / int(num1))


    print(numStack)
    return int(eval(str(numStack[0])))


# print(evalRPN(["1", "2", "+", "3", "*", "4", "-"]))
# print(
#     evalRPN(
#         tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
#     )
# )
print(evalRPN(["1","2","+","3","*","4","-"]))
# print(evalRPN(["4","13","5","/","+"]))
#     validNums = []
#     operands = []
#     expression = "("
#     finalExpression = ""

#     for i in range(len(tokens)):
#         try:
#             float(tokens[i])  # .isdigit() or tokens[i].isnumeric():
#             validNums.append(int(tokens[i]))
#         except:
#             operands.append(tokens[i])

#     for num , op in zip(validNums, operands):
#             if op =="#" or op =="/":
#                 expression += "("
#             expression += str(num) + op

#     expression += str(validNums[-1])+")"
#     print("validNums", validNums, "operands", operands, "expression", expression)

#     for s in range(len(expression)):
#         if expression[s] == "#" or expression[s] == "/":
#             expression = "("+expression[:s] + ")" + expression[s:]

# #add ()


#     return eval(expression)
# for s in range(len(expression))


# for numPos in range(len(validNums) - 1):
#     for operandPos in range(len(operands) - 1):
#         if operands[operandPos] == "/" or operands[operandPos] == "*":
#             expression = "("+finalExpression+(
#                 "("
#                 + str(validNums[numPos])
#                 + operands[operandPos]
#                 + str(validNums[numPos + 1])
#                 + ")"
#             )+")"
#         else:
#             expression += (
#             "("
#             + str(validNums[numPos])
#             + operands[operandPos]
#             + str(validNums[numPos + 1])
#             + ")"
#         )
#         finalExpression += expression+ operands[operandPos+1]
#         numPos+=2
#         operandPos+=2

#         # validNums.pop(numPos)
#         # validNums.pop(numPos + 1)
#         # operands.pop(operandPos)
#         # operands.pop(operandPos + 1)
#         break
#     # continue

#     # print(operands, validNums)
# finalExpression += expression
# print("expression", expression)
# print("finalExpression", finalExpression)
