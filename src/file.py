#!/usr/bin/python3

class File:

	def __init__(self, filename):
		self._state = 0
		self._size = 0
		self.readFile(filename)

	def readFile(self,filename):
		self._file = open(filename)
		self._lines = self._file.readlines()
		self._size = len(self._lines)

	def getLine(self):
		if (self._state < self._size):
			line = self._lines[self._state]
			line = line.split()
			self._state += 1
			return line
		return None

	def closeFile(self):
		self._file.close()