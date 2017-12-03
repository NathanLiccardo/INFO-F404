#!/usr/bin/python3

from .stack import Stack

class Simulator:

	def __init__(self, tasks):
		self._tasks = tasks

	# Structure[i] = [WCET, Period, Deadline, CurrentAdv, WaitingFrom]
	def plot(self, start, stop):
		self.initStructure()
		time = start
		current = 0
		while( time < stop ):
			deadlines = self.checkDeadlines(time)
			arrivals = self.checkArrivals(time)

			index = self.getNext()
			if (index != current):
				self.printInterval(time, current, start)
				start = time
				current = index
			arrivals += deadlines
			for i in arrivals:
				print(i)
			self.updateSystem(index)
			time += 1
		deadlines = self.checkDeadlines(time)
		for i in deadlines:
			print(i)

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
		arrivals = []
		for index in range(len(self._structure)):
			current = self._structure[index]
			counter = self._counterJobs[index]
			if ((current[3] == current[0] and current[4] == current[1]) or \
				(current[3] == 0 and current[4] == 0)):
				arrivals.append(self.arrivalText(time, current, index, counter))
		return arrivals


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
		deadlines = []
		for index in range(len(self._structure)):
			current = self._structure[index]
			counter = self._counterJobs[index]

			# Check missing deadline
			if (current[3] < current[0] and current[4] == current[2]):
				deadlines.append(self.deadlinemissText(time, index, counter))

			# Check task complete
			if (current[3] == current[0] and current[4] == current[1]):
				self._counterJobs[index] += 1
				deadlines.append(self.deadlineText(time, index, counter))
				self._structure[index][3:] = [0,0]
		return deadlines

	def updateSystem(self, index):
		for i in range(len(self._structure)):
			if (index != None and i == index):
				self._structure[index][3] += 1
			self._structure[i][4] += 1


	# Print results

	# Print results
	def printInterval(self, time, index, start):
		if (index != None):
			print(str(start)+"-"+str(time), end="")
			print(": T"+str(index+1), end="")
			print("J"+str(self._counterJobs[index]+1))

	def deadlinemissText(self, time, index, counter):
		return (str(time)+" : Job T"+str(index+1)+"J"+str(counter)+" : misses a deadline")

	def deadlineText(self, time, index, counter):
		return (str(time)+" : Deadline of job T"+str(index+1)+"J"+str(counter+1))

	def arrivalText(self, time, current, index, counter):
		return (str(time)+" : Arrival of job T"+str(index+1)+"J"+str(counter+1))
