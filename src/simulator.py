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

	def checkInterrupt(self, indexCurrent):
		for index in len(self._deadlines):
			self._deadlines[index][0] += 1
			save1 = self._deadlines[index][0]
			save2 = self._deadlines[index][1]
			if (index < indexCurrent):
				if (save1 == save2):
					self._interrupt = True
					self._interruptIndex = index
					self._deadlines[index][0] = 0
			if (index == indexCurrent):
				if (save1 == save2):
					self._deadlines[index][0] = 0
			if (index > indexCurrent):
				if (save1 == save2):
					print("Miss a deadline")


	def plotResult(self):
		timeCurrent,indexCurrent = 0,0
		time,current = self._start,self._tasks[indexCurrent]
		self._interrupt,self._deadlines = False,[]

		for index in len(self._tasks):
			startVal = 0
			deadline = self._tasks.getDeadline()
			self._deadlines.append([startVal,deadline])

		while (time < self._stop):
			while( !self._interrupt and timeCurrent < current.getWcet()):
				time += 1
				timeCurrent += 1
				self.checkInterrupt(indexCurrent)
			if (self._interrupt):
				self._interrupt = False
				timeCurrent = 0
				indexCurrent = self._interruptIndex
			else:
				if (indexCurrent == len(self._tasks)-1):
					indexCurrent = 0
				else:
					indexCurrent += 1

	def printResultsS(self):
		for index in range(len(self._resultS)):
			print("S"+str(index+1)+" "+str(self._resultS[index]))
		print("Interval : [", end="")
		print(str(self._interval[0]), end="")
		print(","+str(self._interval[1])+")")

	def printResultU(self):
		print("Utilisation : ", end="")
		print(str(self._use))
