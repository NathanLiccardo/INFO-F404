#!/usr/bin/python3

class Audsley:

	def __init__(self,tasks):
		self._tasks = tasks

	def gcd(self,valA, valB):
		while valB != 0:
			valA,valB = valB, valA%valB
		return valA

	def lcm(self,values):
		while len(values) > 1:
			valA = values[0]
			valB = values[1]
			values = values[1:]
			values[0] = valA*valB / self.gcd(valA, valB) 
		return values[0]

	def getOmax(self):
		offsets = []
		for task in self._tasks:
			offsets.append(task.getOffset())
		return max(offsets)

	def getLcmPeriod(self):
		period = []
		for task in self._tasks:
			period.append(task.getPeriod())
		return self.lcm(period)

	def feasibility(self):
		self._Omax = int(self.getOmax())
		self._Plcm = self.getLcmPeriod()
		self._Plcm = int(self._Omax+(2*self._Plcm))
		print(str(self._Omax)+" , "+str(self._Plcm))