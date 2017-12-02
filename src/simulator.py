#!/usr/bin/python3

from stack import Stack

class Simulator:

	def __init__(self, start, stop, tasks):
		self._start = start
		self._stop = stop
		self._tasks = tasks
		self._inerval = [0]

	def getTopValue(self, value):
		if (value % 1) > 0:
			return int(value)+1
		return int(value)

	def calculateS(self, period):
		self._resultS = []
		self._resultS.append(self._tasks[0].getOffset())
		for index in range(1,len(self._tasks)):
			offset = self._tasks[index].getOffset()
			period = self._tasks[index].getPeriod()
			previous = self._resultS[-1]
			maxPrevious = max(previous - offset, 0)
			topValue = self.getTopValue( maxPrevious / period )
			Si = offset + (topValue*period)
			self._resultS.append(Si)
		self._interval = [0, self._resultS[-1]+period]

	def utilisation(self):
		self._use = 0
		for index in range(len(self._tasks)):
			task = self._tasks[index]
			Ci = task.getWcet()
			Ti = task.getPeriod()
			self._use += Ci/Ti


	# Structure[i] = [WCET, Period, Deadline, CurrentAdv, WaitingFrom]
	def plot(self):
		self.initStructure()
		time = self._interval[0]
		stop = self._interval[1]
		current = 0
		start = 0
		while( time < stop ):
			self.checkArrivals(time)
			self.checkDeadlines(time)

			index = self.getNext()
			if (index != current):
				self.printInterval(time, current, start)
				start = time
				current = index
			self.updateSystem(index)
			time += 1

	def initStructure(self):
		self._counterJobs = []
		self._structure = []
		for index in range(len(self._tasks)):
			current = []
			current.append(self._tasks[index].getWcet())
			current.append(self._tasks[index].getPeriod())
			current.append(self._tasks[index].getDeadline())
			current.append(0)
			current.append(0)
			self._structure.append(current)
			self._counterJobs.append(0)

	def checkArrivals(self, time):
		for index in range(len(self._structure)):
			current = self._structure[index]
			counter = self._counterJobs[index]
			if ((current[3] == current[0] and current[4] == current[1]) or \
				(current[3] == 0 and current[4] == 0)):
				self.printArrival(time, current, index, counter)

	def getNext(self):
		for index in range(len(self._structure)):
			current = self._structure[index]
			# Check WCET
			if (current[3] >= 0 and current[3] < current[0]):
				return index
			# Check Period
			if (current[3] == current[1]):
				return index
		return None

	def checkDeadlines(self, time):
		for index in range(len(self._structure)):
			current = self._structure[index]
			counter = self._counterJobs[index]

			# Check missing deadline
			if (current[3] < current[0] and current[4] == current[2]):
				self.printDeadlineMiss(time, index, counter)

			# Check task complete
			if (current[3] == current[0] and current[4] == current[1]):
				self._counterJobs[index] += 1
				self.printDeadline(time, index, counter)
				self._structure[index][3:] = [0,0]

	def updateSystem(self, index):
		for i in range(len(self._structure)):
			if (index != None and i == index):
				self._structure[index][3] += 1
			self._structure[i][4] += 1


	# Print results

	def printInterval(self, time, index, start):
		if (index != None):
			print(str(start)+"-"+str(time), end="")
			print(": T"+str(index+1), end="")
			print("J"+str(self._counterJobs[index]+1))

	def printDeadlineMiss(self, time, index, counter):
		print(str(time)+" : Job T", end="")
		print(str(index+1)+"J"+str(counter), end="")
		print(" : misses a deadline")

	def printDeadline(self, time, index, counter):
		print(str(time)+" : Deadline of job T", end="")
		print(str(index+1)+"J"+str(counter-1))

	def printArrival(self, time, current, index, counter):
		print(str(time)+" : Arrival of job T"+str(index+1)+"J"+str(counter+1))

	def printResultsS(self):
		for index in range(len(self._resultS)):
			print("S"+str(index+1)+" "+str(self._resultS[index]))
		print("Interval : [", end="")
		print(str(self._interval[0]), end="")
		print(","+str(self._interval[1])+")")

	def printResultU(self):
		print("Utilisation : ", end="")
		print(str(self._use))