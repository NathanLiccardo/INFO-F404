#!usr/bin/python3

class Job:

    def __init__(self):
        self._id = 0
        self._deadline = 0
        self._wcet = 0
        self._job = 1
        self._execution = 0
        self._waitingTime = 0
        self._arrivalTime = 0

    # Setters
    def setTask(self,task):
        self._id = task.getId()
        self._deadline = task.getDeadline()
        self._wcet = task.getWcet()
        self._job = task.getNextJob()

    def incrementTime(self,i):
        self._waitingTime += i

    def incrementExecution(self,i):
        self._execution += i

    def setArrivalTime(self,time):
        self._arrivalTime = time

    # Getters
    def getId(self):
        return self._id

    def getTime(self):
        return self._waitingTime

    def getExecution(self):
        return self._execution

    def getJob(self):
        return self._job

    def getArrival(self):
        return self._arrivalTime

    # Verifications
    def checkArrival(self):
        return (self._waitingTime == 0)

    def checkDeadline(self):
        return (self._deadline == self._waitingTime)

    def checkComplete(self):
        return (self._wcet == self._execution)

    def timeOver(self):
        return (self._deadline <= self._waitingTime)

    # Get verifications texts
    def getArrivalText(self):
        time = str(self._arrivalTime)
        return (time+": Arrival of job T"+str(self._id)+"J"+str(self._job))

    def getDeadlineText(self):
        time = str(self._arrivalTime+self._waitingTime)
        return (time+": Deadline of job T"+str(self._id)+"J"+str(self._job))

    def getDeadlineMissText(self):
        time = str(self._arrivalTime+self._waitingTime)
        return (time+": Job T"+str(self._id)+"J"+str(self._job)+" : misses a deadline")

    # Job : to string
    def toString(self):
        return (str(self._deadline)+" "+str(self._wcet)+" "+str(self._waitingTime)+" "+str(self._execution))
