#!/usr/bin/python3

from file import File
from feasibility import Feasibility
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
		# Execute audsley algorithm
		_audsley = Audsley()
		_audsley.audsley(_tasks)
	else:
		print("Arg file is missing")

if __name__ == '__main__':
  main()
