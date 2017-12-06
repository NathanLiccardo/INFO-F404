#!/usr/bin/python3

from Files.file import File
from Files.task import Task

from Feasibility.feasibility import Feasibility

from Simulator.feasibilityInterval import FeasibilityInterval
from Simulator.simulator import Simulator

from Audsley.audsley import Audsley

from Plotter.plotter import Plotter

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
		#_interval = (FeasibilityInterval(_feasibility.getPeriod,_tasks)).getInterval()
		#_simulator = Simulator(_tasks)
		#_simulator.printResult(_interval[0],_interval[1],"hard")
		#_simulator.printResult(0,400,"hard")

		# Execute audsley algorithm
		_audsley = Audsley()
		_audsley.audsley(_tasks, [0,400])

		# Plot the result
		#_schedule = _simulator.getSchedule(_interval[0],_interval[1],"hard")
		#_plotter = Plotter(_tasks,_schedule,_interval)

	else:
		print("Arg file is missing")

if __name__ == '__main__':
  main()
