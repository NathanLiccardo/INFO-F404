#!/usr/bin/python3

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

class Plotter:

    def __init__(self,tasks,schedule,interval):
        self.setCanevas(tasks,schedule,interval)
        #self.initData(tasks,schedule,interval)
        self.show()

    def setCanevas(self,tasks,schedule,interval):
        figure = plt.figure()
        self.fig = figure.add_subplot(211)
        self.fig.set_ylim(0,len(tasks)+1)
        self.fig.set_xlim(0,interval[1])
        self.fig.spines['right'].set_visible(False)
        self.fig.spines['top'].set_visible(False)
        self.fig.yaxis.set_ticks_position('left')
        self.fig.xaxis.set_ticks_position('bottom')
        self.fig.set_ylabel("Tasks", size=14, rotation=90)
        self.fig.set_xlabel("Time", size=14, rotation=0)
        self.treatSchedule(schedule)
        loc = plt.MultipleLocator(base=10.0)
        self.fig.xaxis.set_major_locator(loc)

    def show(self):
        pp = PdfPages('save.pdf')
        pp.savefig()
        pp.close()
        plt.show()

    def treatSchedule(self,schedule):
        for i in schedule:
            type = (i.split(" "))[1]
            if (type == "Deadline"):
                start = int(((i.split(" "))[0])[:-1])
                end = int(((i.split(" "))[4])[1])
                self.fig.arrow(start, end, 0, -0.8, head_width=2.5, head_length=0.2, fc='k', ec='k')
            elif (type[0] == 'T'):
                startEnd = (((i.split(" "))[0])[:-1]).split("-")
                start = int(startEnd[0])
                end = int(startEnd[1])
                task = int((((i.split(" "))[1])[1]))
                valX = [start,end]
                valY1 = [task,task]
                valY2 = [task-1,task-1]
                self.fig.fill_between(valX,valY1,valY2,color='b',edgeColor="b")
