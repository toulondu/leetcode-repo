# class MinStack(object):

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         self.minValue = float('inf')

#     def push(self, x):
#         """
#         :type x: int
#         :rtype: None
#         """
#         self.stack.append(x)
#         if x<self.minValue:
#             self.minValue = x


#     def pop(self):
#         """
#         :rtype: None
#         """
#         pop_value = self.stack.pop()
#         if pop_value == self.minValue:
#             self.minValue = self.find_min()
#         return pop_value

#     def top(self):
#         """
#         :rtype: int
#         """
#         return self.stack[-1]


#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return self.minValue
    
#     def find_min(self):
#         min_value = float('inf') 
#         for i in self.stack:
#             if(i < min_value):
#                 min_value = i
#         return min_value

class MinStack(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.head is None:
            self.head = Node(x,x,None)
        else:
            self.head = Node(x,min(self.head.min_value,x),self.head)


    def pop(self):
        """
        :rtype: None
        """
        self.head = self.head.next

    def top(self):
        """
        :rtype: int
        """
        return self.head.val

    def getMin(self):
        """
        :rtype: int
        """
        return self.head.min_value


class Node(object):
    def __init__(self,val,min_value,next_node):
        self.val = val
        self.min_value = min_value
        self.next = next_node

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
print(obj.pop())
print(obj.top())
print(obj.getMin())

