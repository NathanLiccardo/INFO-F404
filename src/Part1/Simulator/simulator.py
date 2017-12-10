#!/usr/bin/python3

from .stack import Stack
from Files.job import Job

class Simulator:

	def __init__(self, tasks):
		self._tasks = tasks
		self._structure = []

	def plot(self,start,stop,type):
		result = []
		time = start
		current = None
		while (time < stop):
			arrivals = self.checkArrivals1(time)
			arrivals += self.checkDeadlines1(time,type)

			index = self.getNext1(time)
			if (index != current and current != None):
				result.append(self.intervalText(current,time,start))
			if (index != current):
				start = time
				current = index

			result += arrivals
			self.updateSystem1(index,time)
			time += 1

		deadlines = self.checkDeadlines1(time,type)
		return result+deadlines

	def checkArrivals1(self,time):
		arrivals = []
		for index in range(len(self._tasks)):
			task = self._tasks[index]
			if (task.periodicalEvent(time) and task.isAvailabe(time)):
				job = Job()
				job.setTask(task)
				job.setArrivalTime(time)
				self._structure.append(job)
				arrivals.append(self.arrivalText(job))
			self._tasks[index] = task
		return arrivals

	def getNext1(self,time):
		current = None
		if (len(self._structure) > 0):
			for job in self._structure:
				if (current == None and not(job.checkComplete())):
					current = job
				elif (current != None and job.getId() < current.getId() and not(job.checkComplete())):
					current = job
		return current

	def checkDeadlines1(self,time,type):
		deadlines = []
		index = 0
		while (index < len(self._structure)):
			job = self._structure[index]
			# Job deadline
			if (job.checkDeadline()):
				deadlines.append(self.deadlineText(job))
			if (not(job.checkComplete()) and job.timeOver()):
				deadlines.append(self.deadlineMissText(job))
			# task reset
			if (job.timeOver() and (job.checkComplete() or type == "hard")):
				self._structure.remove(job)
				index -= 1
			index += 1
		return deadlines

	# Update the system : 1 time over
	def updateSystem1(self,current,time):
		for index in range(len(self._structure)):
			job = self._structure[index]
			if (job == current):
				job.incrementExecution(1)
			job.incrementTime(1)
			self._structure[index] = job

	# Get results
	def printResult(self,start,stop,type):
		print("".join(self.plot(start,stop,type)),end="")

	def intervalText(self,job,time,start):
		return (str(start)+"-"+str(time)+": T"+str(job.getId())+"J"+str(job.getJob())+"\n")

	def deadlineMissText(self,job):
		return (job.getDeadlineMissText()+"\n")

	def deadlineText(self,job):
		return (job.getDeadlineText()+"\n")

	def arrivalText(self,job):
		return (job.getArrivalText()+"\n")

	def getSchedule(self,interval0,interval1,type):
		result = self.plot(interval0,interval1,type)
		return result
