#!/usr/bin/python3

from .stack import Stack

class Simulator:

	def __init__(self, tasks):
		self._tasks = tasks

	def plot(self,start,stop,typeDeadline):
		result = []
		current = None
		time = start
		self.initStructure()
		while (time < stop):

			deadlines = self.checkDeadlines(time,typeDeadline)
			arrivals = self.checkArrivals(time)
			arrivals = arrivals+deadlines

			index = None
			index = self.getNext(time)
			if (index != current and current != None):
				result.append(self.intervalText(time, current, start))
			if (index != current):
				start = time
				current = index

			result += arrivals
			self.updateSystem(index,time)
			time += 1

		deadlines = self.checkDeadlines(time,typeDeadline)
		return result+deadlines

	def initStructure(self):
		self._structure = []
		for index in range(len(self._tasks)):
			self._structure.append(self._tasks[index])

	def checkArrivals(self, time):
		arrivals = []
		for task in self._structure:
			if (task.checkArrival(time)):
				task.resetCounter()
				arrivals.append(self.arrivalText(task,time))
		return arrivals

	def getNext(self,time):
		for task in self._structure:
			if (task.wcetNotCompleted() and task.isAvailabe(time)):
				return task
			if (task.periodicalEvent() and task.isAvailabe(time)):
				return task
		return None

	def checkDeadlines(self,time,type):
		deadlines = []
		for task in self._structure:
			# End of the deadline
			if (task.getWatingTime() == task.getDeadline()):
				deadlines.append(self.deadlineText(task,time))
			# Task not completed
			if (not(task.isComplete) and task.getWatingTime() > task.getDeadline()):
				deadlines.append(self.deadlineMiss(task,time))
		return deadlines

	# Update the system : 1 time over
	def updateSystem(self,task,time):
		for index in range(len(self._structure)):
			t = self._structure[index]
			if (task != None and t.getId() == task.getId()):
				t.setExecution(1)
			if (t.isAvailabe(time)):
				t.setWaitingTime(1)
			self._structure[index] = t

	# Get results
	def printResult(self,start,stop,type):
		print("".join(self.plot(start,stop,type)),end="")

	def intervalText(self,time,task,start):
		return (str(start)+"-"+str(time)+": T"+str(task.getIndex())+"J"+str(task.getJob())+"\n")

	def deadlineMiss(self,task,time):
		return (str(time)+task.getDeadlineMiss()+"\n")

	def deadlineText(self,task,time):
		return (str(time)+task.getDeadlineText()+"\n")

	def arrivalText(self,task,time):
		return (str(time)+task.getArrivalText()+"\n")

	def getSchedule(self,interval0,interval1,type):
		result = self.plot(interval0,interval1,type)
		return result
