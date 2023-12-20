# RTSA-lab02-SchedulabilityTest
In this lab session you will learn how to implement the schedulability tests for:

  * Liu and Layland Bound
  * Time Demand Analysis

All Tasks are periodic, preemptable, fixed priority Tasks with implicit Deadlines.

The task sets are defined int the text files in 'task_sets/'.

## Implementing the Tests

The tests  can be found in 'schedTests/' folder in their corresponding files.
The test() functions are called, if the test was successful it should return True, otherwise False. For the TDA test the code for sorting the task set is already included, so the task set is ordered by highest priority first.

The tasksets are represented by a 2D array, where row i is a Task i and the columns contain period(P_i), Deadline (D_i) and WCET (C_i). This is stated in each file with a large comment and examples are given.


## Runing the Tests

Make sure you have at least python3, argparse, numpy and tabulate installed.
Argpoarse, Numpy and Tabulate can be installed via pip.

Use the SchedTest.py Script

```
usage: SchedTest.py [-h] --i I --n N

A small Scheduling test Framework.

options:
  -h, --help  show this help message and exit
  --i I       Path to the file containing task sets.
  --n N       Number of tasks per set.
```

N is always and defaults to 10, for our input files.

## Correct outputs for evaluation
```
10Tasks
╒═════╤══════╤═══════╤══════╤═══════╕
│   # │    U │   LLB │   HB │   TDA │
╞═════╪══════╪═══════╪══════╪═══════╡
│   0 │ 0.55 │     1 │    1 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│   1 │ 0.58 │     1 │    1 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│   2 │ 0.61 │     1 │    1 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│   3 │ 0.64 │     1 │    1 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│   4 │ 0.67 │     1 │    1 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│   5 │ 0.7  │     1 │    1 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│   6 │ 0.73 │     0 │    1 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│   7 │ 0.76 │     0 │    0 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│   8 │ 0.79 │     0 │    0 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│   9 │ 0.82 │     0 │    0 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│  10 │ 0.85 │     0 │    0 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│  11 │ 0.88 │     0 │    0 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│  12 │ 0.91 │     0 │    0 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│  13 │ 0.94 │     0 │    0 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│  14 │ 0.97 │     0 │    0 │     0 │
├─────┼──────┼───────┼──────┼───────┤
│  15 │ 1    │     0 │    0 │     0 │
╘═════╧══════╧═══════╧══════╧═══════╛
100Tasks
╒═════╤══════╤═══════╤══════╤═══════╕
│   # │    U │   LLB │   HB │   TDA │
╞═════╪══════╪═══════╪══════╪═══════╡
│   0 │ 0.55 │     1 │    1 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│   1 │ 0.58 │     1 │    1 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│   2 │ 0.61 │     1 │    1 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│   3 │ 0.64 │     1 │    1 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│   4 │ 0.67 │     1 │    1 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│   5 │ 0.7  │     0 │    0 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│   6 │ 0.73 │     0 │    0 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│   7 │ 0.76 │     0 │    0 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│   8 │ 0.79 │     0 │    0 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│   9 │ 0.82 │     0 │    0 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│  10 │ 0.85 │     0 │    0 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│  11 │ 0.88 │     0 │    0 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│  12 │ 0.91 │     0 │    0 │     1 │
├─────┼──────┼───────┼──────┼───────┤
│  13 │ 0.94 │     0 │    0 │     0 │
├─────┼──────┼───────┼──────┼───────┤
│  14 │ 0.97 │     0 │    0 │     0 │
├─────┼──────┼───────┼──────┼───────┤
│  15 │ 1    │     0 │    0 │     0 │
╘═════╧══════╧═══════╧══════╧═══════╛
```

## Setup
I guess everyone has a running python setup on his machine.
If not follow this [guide](https://code.visualstudio.com/docs/python/python-tutorial).

But we recommend VS Code, as debug tasks are provided in this repo.
Also make sure to install the python and pylance extension in VS Code.
