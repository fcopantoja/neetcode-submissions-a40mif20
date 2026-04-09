class MyQueue:

    def __init__(self):
        self.stack = []
        self.rstack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        if not self.rstack:
            while self.stack:
                self.rstack.append(self.stack.pop())
        
        return self.rstack.pop()


    def peek(self) -> int:
        if not self.rstack:
            while self.stack:
                self.rstack.append(self.stack.pop())
        
        return self.rstack[-1]
        

    def empty(self) -> bool:
        return not self.stack and not self.rstack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()