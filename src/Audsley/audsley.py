#!/usr/bin/python3

from Simulator.simulator import Simulator

import itertools

class Audsley:

	def __init__(self):
		self._space = 0

	def getAllPossibility(self,tasks,task):
		result = []
		for item in list(itertools.permutations(tasks)):
			result.append(list(item)+[task])
			for index in range(len(result[-1])):
				result[-1][index].setId(index+1)
		return result

	def resetTask(self, tasks, task):
		for index in range(len(tasks)):
			tasks[index].resetAll()
		return (tasks, task)


	def noMissIn(self,result, task):
		for line in result:
			if (("T"+str(task.getId()) in line) and ("misses" in line)):
				return False
		return True

	def isLowestPriorityViable(self,tasks,task,interval):
		allPossibilities = self.getAllPossibility(tasks,task)
		for current in allPossibilities:
			simulation = Simulator(current)
			simulation = simulation.getSchedule(interval[0],interval[1],"soft")
			tasks, task = self.resetTask(tasks, task)
			if (self.noMissIn(simulation,task)):
				return True
		return False

	def audsley(self, tasks, interval):
		for index in range(len(tasks)):
			task = tasks[index]
			tasks.remove(tasks[index])
			if (self.isLowestPriorityViable(tasks, task, interval)):
				task.setId(index+1)
				self.printIsLowest(task)
				self._space += 1
				self.audsley(tasks,interval)
				self._space -= 1
			else:
				task.setId(index+1)
				self.printIsNotLowest(task)
			tasks.insert(index,task)

	# Print Results
	def printIsLowest(self,task):
		print(self._space*" ", end="")
		print("Task "+str(task.getId()), end="")
		print(" : is lowest priority viable ")

	def printIsNotLowest(self,task):
		print(self._space*" ", end="")
		print("Task "+str(task.getId()), end="")
		print(" : is not lowest priority viable")
