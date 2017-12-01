#!/usr/bin/python3

from task import Task

class File:

	def __init__(self, filename):
		self._state = 0
		self._size = 0
		self.readFile(filename)

	def readFile(self,filename):
		self._file = open(filename)
		self._lines = self._file.readlines()
		self._size = len(self._lines)

	def getTasks(self):
		_tasks = []
		_line = self.getLine()
		while _line != None:
			_tasks.append(Task(self._state, _line))
			_line = self.getLine()
		return _tasks

	def getLine(self):
		if (self._state < self._size):
			line = self._lines[self._state]
			line = line.split()
			self._state += 1
			return line
		return None

	def close(self):
		self._file.close()
