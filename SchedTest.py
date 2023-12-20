import argparse
import numpy as np
from tabulate import tabulate

import schedTests.LiuAndLaylandBound as LLB
import schedTests.TimeDemandAnalysis as TDA
import schedTests.HyperbolicBound as HB
import include.TasksHelper as TH
import task_sets.TaskSetGenerator as gen
# This function Parses the Input Arguments


def parse_args():
    # Instantiate the parser
    parser = argparse.ArgumentParser(
        description='A small Scheduling test Framework.')

    # Required argument
    parser.add_argument('--i', type=str, required=True,
                        help='Path to the file containing task sets.')
    # Required argument
    parser.add_argument('--n', type=int, required=False, default=10,
                        help='Number of tasks per set.')

    return parser.parse_args()

# Read Tasksets in to numpy array from text files


def get_tasksets(filename: str, NrSets: int):
    input = np.genfromtxt(filename, dtype=float, delimiter=",", comments=";")
    shape = input.shape
    tasksets = input.reshape(int(shape[0]/NrSets), NrSets, 3)
    return tasksets


def main():
    # Parse Arguments
    args = parse_args()
    print(args.i)
    #np.set_printoptions(threshold=np.inf)
    # Read Tasksets from txt files
    tasksets = get_tasksets(args.i, args.n)
    #tasksets = gen.gen_np_taskset(100)
    print("Successfully parsed Task Sets")
    shape = tasksets.shape
    print("Nr. of Task Sets:     " + str(shape[0]))
    print("Nr. of Tasks per Set: " + str(shape[1]))

    # Starting the analysis
    print("Starting Liu and Layland bound analysis!")
    stubLLB = []
    stubU = []
    for k in range(shape[0]):
        stubLLB.append(False)
        stubU.append(TH.getTotalUtilization(tasksets[k], shape[1]))
    LLBresults = np.array(stubLLB)
    U = np.array(stubU)
    for i in range(shape[0]):
        if LLB.test(tasksets[i]):
            LLBresults[i] = True
            # print("Task Set: " + str(i) +
            #       " fulfills necessary the Liu and Layland Bound!")
    #print()

    print("Starting Hyperbolic bound analysis!")
    stubHB = []
    for _ in range(shape[0]):
        stubHB.append(False)
    HBresults = np.array(stubHB)
    for i in range(shape[0]):
        if HB.test(tasksets[i]):
            HBresults[i] = True
            # print("Task Set: " + str(i) +
            #       " fulfills the sufficient Hyperbolic Bound!")
    #print()

    print("Starting Time Demand Analysis!")
    stubTDA = []
    for _ in range(shape[0]):
        stubTDA.append(False)
    TDAresults = np.array(stubTDA)
    for i in range(shape[0]):
        if TDA.test(tasksets[i]) > 0:
            TDAresults[i] = True
            #print("Task Set: " + str(i) + " is feasible by TDA analysis!")

    #print results
    headers = ["#", "U", "LLB", "HB", "TDA"]
    # Generate the table in fancy format.
    results = np.array((np.arange(shape[0]), U, LLBresults, HBresults, TDAresults)).T
    table = tabulate(results, headers, tablefmt="fancy_grid")
    print(table)



if __name__ == "__main__":
    main()
