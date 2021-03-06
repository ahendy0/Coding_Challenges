class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.s1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.shift()
        return self.s2.pop()
    
    def peek(self):
        """
        :rtype: int
        """
        self.shift()
        return self.s2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.s1) == 0 and len(self.s2) == 0
        
    def shift(self):
        if not self.s2:
            while len(self.s1) > 0:
                q = self.s1.pop()
                self.s2.append(q)

