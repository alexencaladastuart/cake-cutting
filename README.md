# Fair Cake-Cutting Algorithms

Alex Encalada-Stuart, Alison Simons, and Vera Zhou

Final project for CS 136, Fall 2021

***

### Summary

Computer scientists have long studied the problem of dividing a cake fairly among a group of *n* people. Two common design goals are fairness (which means each agent gets 1/*n* of the cake by their own measure) and envy-freeness (which means each agent wouldn't rather have another agent's piece of cake). Our project simulates three cake-cutting algorithms: the last-diminisher procedure, Stormquist's moving-knives procedure, and the recursive halving procedure. These algorithms are designed to allocate subsections of a line segment from 0 to 1 in a way that approximates fairness for the agents. Summary statistics are printed at the end of the simulation for analysis.

### Usage

To run our simulation, the user should simply type `python3 sim.py` followed by the method to be used, the type of agent and the number of that agent, and various optional parameters. There are three possible agents: 1) the uniform agent, which have a valuation of 1 for every atom of the cake, 2) the random agent, which will randomly assign a value of 0 or 1 to every atom of the cake, and 3) the normalized agent, which will randomly assign a value to every atom of the cake and ensure that the values of all atoms sum to 1. The three possible procedures are last-diminisher, stromquist, and recursive. The user can also specify the log level, the number of pieces of the cake, the number of iterations to run, and the seed used for randomization. For example, if the user wants to run 100 simulations using the last-diminisher procedure with 10 normalized agents, a seed of 0, 500 pieces, and an info log level, they can run the following:
```
python3 sim.py last_diminisher Normalized,10 --seed=0 --num-pieces=500 --loglevel=Info --iters=100
```
The program will output statistics for each agent as overall statistics. For example, the above command will print out the following:
```
=========SUMMARY=========
Agent 0 got 0.10464474107435454 of the cake, did not get a fair proportion 0 of the time, and was envious 0.9600000000000006 of the time
Agent 1 got 0.1085204659365087 of the cake, did not get a fair proportion 0 of the time, and was envious 0.9300000000000006 of the time
Agent 2 got 0.1070979641786067 of the cake, did not get a fair proportion 0 of the time, and was envious 0.9200000000000006 of the time
Agent 3 got 0.10745333496401259 of the cake, did not get a fair proportion 0 of the time, and was envious 0.8800000000000006 of the time
Agent 4 got 0.11023171507811655 of the cake, did not get a fair proportion 0 of the time, and was envious 0.8100000000000005 of the time
Agent 5 got 0.1071195421890139 of the cake, did not get a fair proportion 0 of the time, and was envious 0.9000000000000006 of the time
Agent 6 got 0.10894526661016223 of the cake, did not get a fair proportion 0 of the time, and was envious 0.8500000000000005 of the time
Agent 7 got 0.10968078622491707 of the cake, did not get a fair proportion 0 of the time, and was envious 0.8200000000000005 of the time
Agent 8 got 0.11403558586126383 of the cake, did not get a fair proportion 0 of the time, and was envious 0.7000000000000004 of the time
Agent 9 got 0.11253619530860741 of the cake, did not get a fair proportion 0 of the time, and was envious 0.7500000000000004 of the time
The total welfare is 1.0902655974255644
The average nonproportionality rate is 0.0
The average envy rate is 0.8520000000000006
The worst envy rate is 0.9600000000000006
```
Note 1: Stromquist can only be run with 3 agents.\
Note 2: Recursive halving works best when the number of agents is a power of 2 (i.e. 2, 4, 8, 16, etc.).\
Note 3: If more information is desired, use `--loglevel=Debug`.