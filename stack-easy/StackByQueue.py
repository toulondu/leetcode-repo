# -*- encoding: utf-8 -*-
'''
@FILE           :StackByQueue.py
@TIME           :2020/05/02 15:28:24
@AUTHOR         :Toulon Du
@EMAIL          :seaduhe@gmail.com
@DESCRIPTION    :
@VERSION        :1.0
'''

"""
使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
注意:

你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-stack-using-queues
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import queue

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = queue.Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        # 每次入栈时反转队列元素
        self.queue1.put(x)
        q_size = self.queue1.qsize()
        while q_size>1:
            self.queue1.put(self.queue1.get())
            q_size -=1


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.queue1.get()


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        # py的get会移除元素。。。
        val = self.queue1.get()
        self.push(val)
        return val


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.queue1.qsize() == 0

obj = MyStack()
print(obj.empty())
obj.push(3)
param_2 = obj.pop()
param_3 = obj.top()