#!usr/bin/python3

class Stack:

    def __init__(self):
        self._stack = []
        self._index = 0

    def push(self, value):
        self._stack.append(value)

    def pop(self):
        value = self._stack[-1]
        self._stack = self._stack[:-1]
        return value

    def isEmpty(self):
        return (len(self._stack) == 0)
