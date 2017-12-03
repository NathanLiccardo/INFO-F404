#!/usr/bin/python3

from .stack import Stack

class Simulator:

	def __init__(self, tasks):
		self._tasks = tasks

	"""
	Structure[i] = [WCET, Period, Deadline, CurrentAdv, WaitingFrom]
	"""
	def plot(self, start, stop):
		# Init variable
		current = 0
		time = start
		self.initStructure()
		# Time loop
		while( time < stop ):
			# checkDeadlines and Arrivals
			deadlines = self.checkDeadlines(time)
			arrivals = self.checkArrivals(time)
			arrivals = arrivals+deadlines
			# Apply the run
			index = self.getNext()
			if (index != current and current != None):
				print(self.intervalText(time, current, start), end="")
			if (index != current)
				start = time
				current = index
			#Update the system and print results
			print("".join(arrivals), end="")
			self.updateSystem(index)
			time += 1
		# Check system at the end
		deadlines = self.checkDeadlines(time)
		print("".join(deadlines))

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
	def intervalText(self, time, index, start):
		return (str(start)+"-"+str(time)+": T"+str(index+1)+"J"+str(self._counterJobs[index]+1)+'\n')

	def deadlinemissText(self, time, index, counter):
		return (str(time)+" : Job T"+str(index+1)+"J"+str(counter)+" : misses a deadline"+'\n')

	def deadlineText(self, time, index, counter):
		return (str(time)+" : Deadline of job T"+str(index+1)+"J"+str(counter+1)+'\n')

	def arrivalText(self, time, current, index, counter):
		return (str(time)+" : Arrival of job T"+str(index+1)+"J"+str(counter+1)+'\n')
