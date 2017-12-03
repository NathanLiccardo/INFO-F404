#!/usr/bin/python3

from .stack import Stack

class Simulator:

	def __init__(self, tasks):
		self._tasks = tasks

	"""
	Structure[i] = [WCET, Period, Deadline, CurrentAdv, WaitingFrom]
	"""
	def plot(self, start, stop, typeDeadlines):
		result = []
		# Init variable
		current = 0
		time = start
		self.initStructure()
		# Time loop
		while( time < stop ):
			# checkDeadlines and Arrivals
			if (typeDeadlines == "hard"):
				deadlines = self.checkDeadlinesHard(time)
			else:
				deadlines = self.checkDeadlinesSoft(time)
			arrivals = self.checkArrivals(time)
			arrivals = arrivals+deadlines
			# Apply the run
			index = self.getNext()
			if (index != current):
				if (current != None):
					result += [self.intervalText(time, current, start)]
				start = time
				current = index
			#Update the system and print results
			result += arrivals
			self.updateSystem(index)
			time += 1
		# Check system at the end
		if (typeDeadlines == "hard"):
			deadlines = self.checkDeadlinesHard(time)
		else:
			deadlines = self.checkDeadlinesSoft(time)
		return result+deadlines

	def initStructure(self):
		# Init structure before the execution
		self._structure = [[] for i in range(len(self._tasks))]
		self._counterJobs = [0 for i in range(len(self._tasks))]
		for index in range(len(self._tasks)):
			self._structure[index].append(self._tasks[index].getWcet())
			self._structure[index].append(self._tasks[index].getPeriod())
			self._structure[index].append(self._tasks[index].getDeadline())
			self._structure[index].extend((0,0))

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

	def checkDeadlinesHard(self, time):
		deadlines = []
		for index in range(len(self._structure)):
			current = self._structure[index]
			counter = self._counterJobs[index]

			# Check missing deadline
			if (current[3] < current[0] and current[4] == current[2]):
				self._counterJobs[index] += 1
				deadlines.append(self.deadlinemissText(time, index, counter))
				self._structure[index][3:] = [0,0]

			# Check task complete
			if (current[3] == current[0] and current[4] == current[1]):
				self._counterJobs[index] += 1
				deadlines.append(self.deadlineText(time, index, counter))
				self._structure[index][3:] = [0,0]
		return deadlines

	def checkDeadlinesSoft(self, time):
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


	# Get results
	def printResult(self,start,stop):
		print("".join(self.plot(start,stop,"hard")),end="")

	def intervalText(self, time, index, start):
		return (str(start)+"-"+str(time)+": T"+str(index+1)+"J"+str(self._counterJobs[index]+1)+'\n')

	def deadlinemissText(self, time, index, counter):
		return (str(time)+": Job T"+str(index+1)+"J"+str(counter)+" : misses a deadline"+'\n')

	def deadlineText(self, time, index, counter):
		return (str(time)+": Deadline of job T"+str(index+1)+"J"+str(counter+1)+'\n')

	def arrivalText(self, time, current, index, counter):
		return (str(time)+": Arrival of job T"+str(index+1)+"J"+str(counter+1)+'\n')

	def getSchedule(self,interval0,interval1,type):
		result = self.plot(interval0,interval1,type)
		return result
