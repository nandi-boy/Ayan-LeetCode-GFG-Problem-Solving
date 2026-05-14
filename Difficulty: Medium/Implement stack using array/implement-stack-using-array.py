class myStack:
    def __init__(self, n):
        self.stack = []
        self.size = n
        
    def isEmpty(self):
        return len(self.stack)==0
    
    def isFull(self):
        return len(self.stack)==self.size
    
    def push(self, x):
        if not self.isFull():
            return self.stack.append(x)
    
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
            
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        return -1
        