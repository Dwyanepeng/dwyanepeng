#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 5.py
# Author: PengLei
# Date  : 2019/4/22
'''用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。'''

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        self.stack1.append(node)
    def pop(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return "Queue is empty!"
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop(-1))
        return self.stack2.pop(-1)
s = Solution()
# s.push(1)
s.push(1)
s.push(2)
s.push(3)
print(s.pop())

