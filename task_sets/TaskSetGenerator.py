import numpy as np
import random


###
# Task set generation.
###

# Main functions.

def gen_tasksets(num_tasks, num_tasksets, min_period, max_period, utilization,
                 rounded=False):
    """Generate task sets.
    Variables:
    num_tasks: number of tasks per set
    num_tasksets: number of sets
    min_period: minimal period
    max_period: maximal period
    utilization: desired utilization
    rounded: flag to round periods to integers
    """
    # Create periods.
    tasksets_periods = generate_periods_loguniform(
        num_tasks, num_tasksets, min_period, max_period, rounded)
    # Create utilizations.
    tasksets_utilizations = generate_utilizations_uniform(
        num_tasks, num_tasksets, utilization)
    # Create tasksets by matching both of the above.
    tasksets = []
    tasksetsnp = []
    for i in range(num_tasksets):
        taskset = []
        for j in range(num_tasks):
            task = {
                'execution': (tasksets_periods[i][j]
                              * tasksets_utilizations[i][j]),
                'period': tasksets_periods[i][j],
                'deadline': tasksets_periods[i][j]
            }
            taskset.append(task)
        tasksets.append(taskset)
        tasksetsnp.append(np.array((tasksets_periods[0],tasksets_periods[0], np.array(tasksets_periods[0])*np.array(tasksets_utilizations[0]))).T)
    return np.array(tasksetsnp)

def generate_utilizations_uniform(num_tasks, num_tasksets, utilization):
    """Generate utilizations with UUNIFAST.
    Variables:
    num_tasks: number of tasks per set
    num_tasksets: number of sets
    utilization: desired utilization in (0,1]
    """
    def uunifast(num_tasks, utilization):
        """UUNIFAST utilization pulling."""
        utilizations = []
        cumulative_utilization = utilization
        for i in range(1, num_tasks):
            # Randomly set next utilization.
            cumulative_utilization_next = (
                cumulative_utilization
                * random.random() ** (1.0/(num_tasks-i)))
            utilizations.append(
                cumulative_utilization - cumulative_utilization_next)
            # Compute remaining utilization.
            cumulative_utilization = cumulative_utilization_next
        utilizations.append(cumulative_utilization_next) # type: ignore
        # Return list of utilizations.
        return utilizations
    # Return one list of utilizations for each task set.
    return [uunifast(num_tasks, utilization) for i in range(num_tasksets)]


# help functions

def generate_periods_loguniform(num_tasks, num_tasksets, min_period,
                                max_period, rounded=False):
    """Generate log-uniformly distributed periods to create tasks.
    Variables:
    num_tasks: number of tasks per set
    num_tasksets: number of sets
    min_period: minimal period
    max_period: maximal period
    rounded: flag to round periods to integers
    """
    # Create random periods.
    periods = np.exp(np.random.uniform(
        low=np.log(min_period),
        high=np.log(max_period),
        size=(num_tasksets, num_tasks)))
    # Make list out of them
    if rounded:  # round periods to nearest integer
        return np.rint(periods).tolist()
    else:
        return periods.tolist()


def gen_np_taskset(NrTasks):
    tasksets = []
    for i in range(55,101,3):
        tasksets.append(gen_tasksets(NrTasks,1,1,100,i/100)[0])
    return np.array(tasksets)
