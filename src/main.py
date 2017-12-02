#!/usr/bin/python3

from file import File
from feasibility import Feasibility
from simulator import Simulator
from audsley import Audsley
import sys

def main():
	if (len(sys.argv) == 2):
		# Open file and get tasks
		_file = File(sys.argv[1])
		_tasks = _file.getTasks()
		_file.close()
		# Write feasibility interval
		_feasibility = Feasibility(_tasks)
		_feasibility.printSet()
		# Simulator part
		_start = _feasibility.getStart()
		_stop = _feasibility.getStop()
		_simulator = Simulator(_start, _stop, _tasks)
		_simulator.calculateS(_feasibility.getPeriod())
		_simulator.printResultsS()
		_simulator.utilisation()
		_simulator.printResultU()
		_simulator.plot()
		# Execute audsley algorithm
		#_audsley = Audsley()
		#_audsley.audsley(_tasks)
	else:
		print("Arg file is missing")

if __name__ == '__main__':
  main()
