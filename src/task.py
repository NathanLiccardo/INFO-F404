#!usr/bin/python3

class Task:

	def __init__(self, id, line):
		self._id = id
		self.checkLine(line)

	def checkLine(self, line):
		if len(line) == 4:
			self._offset    = int(line[0])
			self._period    = int(line[1])
			self._deadline  = int(line[2])
			self._wcet 		= int(line[3])
		else:
			print("input file error")

	def setOffset(self, offset):
		self._offset = offset

	def setPeriod(self, period):
		self._period = period

	def setDeadline(self, deadline):
		self._deadline = deadline

	def setWcet(self, wcet):
		self._wcet = wcet

	def getOffset(self):
		return self._offset

	def getPeriod(self):
		return self._period

	def getDeadline(self):
		return self._deadline

	def getWcet(self):
		return self._wcet

	def getIndex(self):
		return self._id
