class myQueue:
    def __init__(self, n):
        self.queue = []
        self.size = n

    
    def isEmpty(self):
        return len(self.queue)==0
    
    def isFull(self):
        return len(self.queue)== self.size

    def enqueue(self, x):
        if not self.isFull():
            self.queue.append(x)
    
    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)

    def getFront(self):
        if not self.isEmpty():
            return self.queue[0]
        return -1 
        
    def getRear(self):
        if not self.isEmpty():
            return self.queue[-1]
        return -1
        
        