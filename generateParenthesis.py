def generateParenthesis( n: int) -> List[str]:
        expr = []
        for comb in product("()", repeat=2 * n):
            joined = ''.join(comb)
            if isValid(joined) and joined not in expr:
                expr.append(joined)
        return expr

    def isValid(s: str) -> bool:
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif not stack or char != stack.pop():
                return False
        return not stack
    #hint : use Catalna number Cn  that's used to count only specific structures (well formed parentheses of n paurs, # of valid binary trees with n+1 leaves + # of ways to trinagulate a polygon with n+2)
    # Cn=(1/n+1)*((2n)!/(n+1)!)
        # possibilities = math.factorial(2*n)//(math.factorial(n)*math.factorial(n+1))
        # expr=[]
        # if n ==1:
        #     return ["()"]
        # for comb in product("()", repeat=2 * n):
        #     if comb not in expr:
        #         expr.append(''.join(comb))
        # return expr
            # possibilities = math.factorial(2*n)//(math.factorial(n)*math.factorial(n+1))
            # i,j =0,0
            # expr=[]
            # if n ==1:
            #     return ["()"]
            # while (i <= possibilities):
            #     parenthesis = ""
            #     while j < n:
            #         parenthesis = "("+parenthesis+")"
            #         j+=1
            #     if parenthesis not in expr: 
            #         expr.append(parenthesis)
            #     j=0
            #     parenthesis = ""
            #     while j < n:
            #         parenthesis = parenthesis+"("+parenthesis+")"
            #         j+=1
            #     # if isValid(parenthesis)  :
            #     if parenthesis not in expr: 
            #         expr.append(parenthesis)
            #     j=0
            #     parenthesis = ""
            #     while j < n:
            #         parenthesis = "("+parenthesis+")"+parenthesis
            #         j+=1
            #     # if isValid(parenthesis)  :
            #     if parenthesis not in expr: 
            #         expr.append(parenthesis)
            #     j=0
            #     parenthesis = ""
            #     while j < n:
            #         parenthesis += parenthesis+parenthesis
            #         j+=1
            #     # if isValid(parenthesis)  :
            #     if parenthesis not in expr: 
            #         expr.append(parenthesis)
            #     j=0
            #     parenthesis = ""
            #     while j < n:
            #         parenthesis += "("+parenthesis+")"
            #         j+=1
            #     # if isValid(parenthesis)  :
            #     if parenthesis not in expr: 
            #         expr.append(parenthesis)
            #     j=0
            #     parenthesis = ""
            #     while j < n:
            #         parenthesis += "("+parenthesis+")"
            #         j+=1
            #     # if isValid(parenthesis)  :
            #     if parenthesis not in expr: 
            #         expr.append(parenthesis)
            #     i+=1
            
            # return expr
