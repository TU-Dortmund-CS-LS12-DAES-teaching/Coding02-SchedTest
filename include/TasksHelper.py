import numpy as np

def getTotalUtilization(tasks, NrTasks):
    U = 0
    for i in range(NrTasks):
        U += tasks[i][2] / tasks[i][1]
    return U

def P_i(tasks, i):
    return tasks[i][0]

def D_i(tasks, i):
    return tasks[i][1]

def C_i(tasks, i):
    return tasks[i][2]

def getNumberOfTasks(tasks):
    return tasks.shape[0]