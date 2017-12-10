#!/usr/bin/python3

class FeasibilityInterval:

    def __init__(self,period,tasks):
        self._period = period
        self._tasks = tasks

    def roundToTop(self, value):
        return int(value)+1 if (value%1) > 0 else int(value)

    def calculateS(self, period):
        #Init result array
        self._resultS = [self._tasks[0].getOffset()]
        # Iterate on all the tasks (2 -> n)
        for index in range(1,len(self._tasks)):
            # Get period and offset from current task
            offset = self._tasks[index].getOffset()
            period = self._tasks[index].getPeriod()
            # Get previous result
            maxPrevious = max(self._resultS[-1] - offset, 0)
            # Get result value and append to the list result
            Si = offset+(self.roundToTop(maxPrevious/period)*period)
            self._resultS.append(Si)
            # Calculate the interval
            self._interval = [0, self._resultS[-1]+period]

    # Get results
    def getInterval(self):
        self.calculateS(self._period)
        return (self._interval)

    # Print results
    def printResultsS(self):
        for index in range(len(self._resultS)):
            print("S"+str(index+1)+" "+str(self._resultS[index]))
        print("Interval : [", end="")
        print(str(self._interval[0]), end="")
        print(","+str(self._interval[1])+")")
