#!/usr/bin/python3

from Files.file import File
from Files.task import Task

from Feasibility.feasibility import Feasibility

from Simulator.feasibilityInterval import FeasibilityInterval
from Simulator.simulator import Simulator

#from audsley import Audsley

import sys

def main():
	if (len(sys.argv) == 2):

		# Open file and get tasks
		_file = File(sys.argv[1])
		_tasks = _file.getTasks()

		# Write feasibility interval
		_feasibility = Feasibility(_tasks)
		_feasibility.printSet()

		# Simulator part
		_interval = (FeasibilityInterval(_feasibility.getPeriod,_tasks)).getInterval()
		_simulator = Simulator(_tasks)
		_simulator.plot(_interval[0], _interval[1])
		# Execute audsley algorithm
		#_audsley = Audsley()
		#_audsley.audsley(_tasks)
	else:
		print("Arg file is missing")

if __name__ == '__main__':
  main()
