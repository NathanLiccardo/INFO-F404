#!usr/bin/python3

class Task:

	def __init__(self, id, line):
		self._id = id
		#self._job = 1
		#self._execution = 0
		#self._waitingTime = 0
		self._numberOfJob = 0
		self.checkLine(line)

	def checkLine(self, line):
		if len(line) == 4:
			self._offset    = int(line[0])
			self._period    = int(line[1])
			self._deadline  = int(line[2])
			self._wcet 		= int(line[3])
		else:
			print("Task creation : error")

	# Setters
	def setId(self, id):
		self._id = id

	def setOffset(self, offset):
		self._offset = offset

	def setPeriod(self, period):
		self._period = period

	def setDeadline(self, deadline):
		self._deadline = deadline

	def setWcet(self, wcet):
		self._wcet = wcet

	# Getters
	def getId(self):
		return self._id

	def getOffset(self):
		return self._offset

	def getPeriod(self):
		return self._period

	def getDeadline(self):
		return self._deadline

	def getWcet(self):
		return self._wcet

	# Get conditions texts
	def toString(self):
		return str(self._offset)+" "+str(self._period)+" "+str(self._deadline)+" "+str(self._wcet)

	# Check conditions
	def isAvailabe(self,time):
		return (self._offset <= time)

	def periodicalEvent(self,time):
		return (((time-self._offset) % self._period) == 0)

	def getNextJob(self):
		self._numberOfJob += 1
		return self._numberOfJob

	def resetAll(self):
		self._numberOfJob = 0
