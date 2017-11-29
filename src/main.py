#!/usr/bin/python3

from file import File
from task import Task
from audsley import Audsley
import sys


def main():
	if (len(sys.argv) == 2):
		_file = File(sys.argv[1])
		_tasks = []
		_line = _file.getLine()
		while _line != None:
			_index = len(_tasks)+1
			_tasks.append(Task(_index, _line))
			_line = _file.getLine()
		_audsley = Audsley(_tasks)
		_audsley.feasibility()
	else:
		print("Arg file is missing")
  
if __name__ == '__main__':
  main()