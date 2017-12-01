#!/usr/bin/python3

class Audsley:

	def __init__(self):
		self._result = []
		self._checked = []
		self._space = 0

	def isLowesPriorityViable(self,task,tasks):
		# TODO : return if the task is LPV
		return True

	def audsley(self, tasks):
		for index in range(len(tasks)-1):
			if (self.isLowesPriorityViable(tasks[index], tasks)):
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
