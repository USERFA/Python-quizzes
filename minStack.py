class MinStack:

    def __init__(self):
        self.stack = [] 

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if(len(self.stack)!=0):
            return self.stack[-1]
        

    def getMin(self) -> int:
        if len(self.stack) != 0:
            return min(self.stack)

mystack = MinStack()
mystack.push(-2)
mystack.push(0)
mystack.push(-3)
print(mystack)
print('min',mystack.getMin())
mystack.pop()
print('top after pop',mystack.top())
print('min',mystack.getMin())
        
