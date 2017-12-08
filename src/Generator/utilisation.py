#!/usr/bin/python3

from random import randint
from Files.task import Task

class Utilisation:

    def __init__(self,numberOfTasks,utilisationFactor):
        self._utilisation = utilisationFactor
        self._numberOfTasks = numberOfTasks
        self._use = self.splitUtilisation()
        self._result = self.findUsage()

    def splitUtilisation(self):
        result = [randint(1,100) for i in range(self._numberOfTasks)]
        ratio = self._utilisation/sum(result)
        result = [round(value*ratio) for value in result]
        return result

    def findSystem(self):
        result = []
        for use in self._use:
            print(use)
            Ti = randint(1,1000)
            Ci = round(use*(Ti/100))
            task = Task()
            task.setAll(0, 0, Ti, random(Ci,Ti), Ci)
            result.append(task)
        return result

    # Print result
    def printUse(self):
        print("Total use : "+str(sum(self._use)), end="")
        print(" ("+" ".join(str(self._use))+")")

    def printSystem(self):
        for task in self._result:
            print(task.toString())
