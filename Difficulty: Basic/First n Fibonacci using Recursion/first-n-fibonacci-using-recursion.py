class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fib(self, n):
        if n <= 1:
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)

    def fibonacciNumbers(self, n):
        arr = []
        for i in range(n):
            arr.append(self.fib(i))
        return arr
        
        
        