class MyQueue(object):

    def __init__(self):
        self._fifo = []

    def push(self, x):
        """
        pushes element x to the back of the queue
        :type x: int
        :rtype: None
        """
        self._fifo.append(x)
        

    def pop(self):
        """
        removes element from front of queue
        :rtype: int
        """
        return self._fifo.pop(0)
        

    def peek(self):
        """
        returns element at front of queue
        :rtype: int
        """
        return self._fifo[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self._fifo   


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()