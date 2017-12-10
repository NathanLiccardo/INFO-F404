#!/usr/bin/python3

from .task import Task

class File:

	def __init__(self, fileName):
		self._state = 0
		self.open(fileName)

	def open(self, fileName):
		_file = open(fileName)
		self._line = _file.readlines()
		_file.close()

	def getTasks(self):
		_tasks = [Task(self.getSate()+1,self.getLine()) for i in self._line]
		return _tasks

	def getSate(self):
		return self._state

	def getLine(self):
		line = (self._line[self._state]).split()
		self._state += 1
		return line
