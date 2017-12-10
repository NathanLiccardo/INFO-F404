#!/usr/bin/python3

class Feasibility:

    def __init__(self,tasks):
        self._tasks = tasks

    def gcd(self,valA, valB):
        while valB != 0:
            valA,valB = valB, valA%valB
        return valA

    def lcm(self,values):
        while len(values) > 1:
            values[1] = values[0]*values[1] / self.gcd(values[0], values[1])
            values = values[1:]
        return values[0]

    def getOmax(self):
        offsets = [i.getOffset() for i in self._tasks]
        return max(offsets)

    def getLcmPeriod(self):
        period = [i.getPeriod() for i in self._tasks]
        return self.lcm(period)

    def getPeriod(self):
        return self.getLcmPeriod()

    def getStart(self):
        return int(self.getOmax())

    def getStop(self):
        return int( (self.getLcmPeriod()*2) + self.getOmax() )

    def printSet(self):
        Omax = int(self.getOmax())
        Plcm = self.getLcmPeriod()
        Plcm = int(Omax+(2*Plcm))
        print("Interval : [", end="")
        print(str(Omax), end="")
        print(","+str(Plcm)+")")
