import numpy as np
import math
import include.TasksHelper as TH

# The tasks is an Array with three columns and n Rows
# Each Row represents one Task
# The columns hold the Tasks parameters
# column 0 is period P,
# column 1 is deadline D
# column 2 is WCET C
# P_i is accessed as: tasks[i][0]
# D_i is accessed as: tasks[i][1]
# C_i is accessed as: tasks[i][2]
# The number of tasks can be accessed as: tasks.shape[0]

#Workload function for task i in ordered tasks
#Will return the Workload or -1 of not feasible
def Workload(tasks, i):
    return -1

#The Time Demand Analysis Test
def test(tasks):
    return False
