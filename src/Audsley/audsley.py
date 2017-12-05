#!/usr/bin/python3

from Simulator.simulator import Simulator

import itertools

class Audsley:

	def __init__(self):
		self._space = 0

	def getAllPossibility(self,tasks):
		return list(itertools.permutations(tasks))

	def noMissIn(self,result, tasks):
		print("".join(result),end="\n")
		for i in result:
			if (("misses" in i) and ("T"+str(tasks) in i)):
				return False
		return True

	def isLowesPriorityViable(self,index,tasks,interval):
		# TODO : return if the task is LPV
		lenTasks = len(tasks)
		save = tasks[index]
		if (index < len(tasks)-1):
			tasks = tasks[:index]+tasks[index+1:]
		else:
			tasks = tasks[:-1]
		permutations = self.getAllPossibility(tasks)
		for i in permutations:
			result = Simulator(list(i)+[save])
			result = result.getSchedule(interval[0],interval[1],"soft")
			if (self.noMissIn(result,lenTasks)): return True
		return False

	def audsley(self, tasks, interval):

		for index in range(len(tasks)):
			if (self.isLowesPriorityViable(index, tasks, interval)):
				print(self._space*" ", end="")
				print("Task "+str(tasks[index].getIndex()), end="")
				print(" : is lowest priority viable")
				self._space += 1
				if (index != len(tasks)-1):
					self.audsley(tasks[:index]+tasks[index+1:],interval)
				else:
					self.audsley(tasks[:index],interval)
				self._space -= 1
			else:
				print(self._space*" ", end="")
				print("Task "+str(tasks[index].getIndex()), end="")
				print(" : is not lowest priority viable")
