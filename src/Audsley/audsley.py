#!/usr/bin/python3

from Simulator.simulator import Simulator

import itertools

class Audsley:

	def __init__(self):
		self._space = 0

	def getAllPossibility(self,tasks):
		return list(itertools.permutations(tasks))

	def noMissIn(self,result, tasks):
		task = "T"+str(tasks)
		for i in result:
			if ("misses" in i and task in i): return False
		return True

	def isLowesPriorityViable(self,index,tasks,interval):
		# TODO : return if the task is LPV
		save = tasks[index]
		if (index < len(tasks)-1):
			tasks = tasks[:index]+tasks[index+1:]+[save]
		for i in self.getAllPossibility(tasks[:-1]):
			result = Simulator(tasks[:-1]+[save])
			result = result.getSchedule(interval[0],interval[1],"soft")
			if (self.noMissIn(result,len(tasks))): return True
		return False

	def audsley(self, tasks, interval):
		for index in range(len(tasks)):
			if (self.isLowesPriorityViable(index, tasks, interval)):
				print(self._space*" ", end="")
				print("Task "+str(tasks[index].getIndex()), end="")
				print(" : is lowest priority viable")
				self._space += 1
				if (index != len(tasks)-1):
					self.audsley(tasks[:index]+tasks[index+1:])
				else:
					self.audsley(tasks[:index])
				self._space -= 1
			else:
				print(self._space*" ", end="")
				print("Task "+str(tasks[index].getIndex()), end="")
				print(" : is not lowest priority viable")
