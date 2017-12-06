#!usr/bin/python3

class Task:

	def __init__(self, id, line):
		self._id = id
		self._job = 0
		self._execution = 0
		self._waitingTime = 0
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

	def setExecution(self, i):
		self._execution += i

	def setWaitingTime(self, i):
		self._waitingTime += i

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

	def getIndex(self):
		return self._id

	def getJob(self):
		return self._job

	def getExecution(self):
		return self._execution

	def getWatingTime(self):
		return self._waitingTime

	# Get conditions texts
	def getArrivalText(self):
		return ": Arrival of job T"+str(self._id)+"J"+str(self._job)

	def getDeadlineMissText(self):
		return ": Job T"+str(self._id)+"J"+str(self._job)+" : misses a deadline"

	def getDeadlineText(self):
		result = ": Deadline of job T"+str(self._id)+"J"+str(self._job)
		return result

	def toString(self):
		return str(self._offset)+" "+str(self._period)+" "+str(self._deadline)+" "+str(self._wcet)

	# Check conditions
	def checkArrival(self, time):
		if (time == self._offset or self._period == self._waitingTime):
			self._job += 1
			return True
		return False

	def deadlineMiss(self):
		return (self._waitingTime >= self._deadline and self._execution < self._wcet)

	def deadline(self):
		return (self._execution == self._wcet and self._waitingTime == self._deadline)

	def wcetNotCompleted(self):
		return (self._execution < self._wcet and self._execution >= 0)

	def isComplete(self):
		return (self._execution == self._wcet)

	def isAvailabe(self,time):
		return (self._offset <= time)

	def periodicalEvent(self):
		return (self._period == self._waitingTime)

	def nextJob(self):
		self._job += 1

	# Reset - New job
	def resetCounter(self):
		self._waitingTime = 0
		self._execution = 0

	def resetAll(self):
		self._waitingTime = 0
		self._execution = 0
		self._job = 0

	def complete(self):
		self._execution = self._wcet
