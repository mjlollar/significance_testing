# Description

This repository contains scripts used to generate p-values using various methods. Most scripts can be run from personal computers, with requirements about the format of inouts (usually files must take the format of a comma-separated file (csv) with headers. Headers are required as input flags are mostly header names for dataset categories. An example of an input file is provided (input_example.csv).
Many of the python scripts can be called with a '--help' flag for information on the exact input requirement (header names) for each script. 

# Repository includes:
 Bootstrap versions include:
5.0 - Combined-cross significance test for 5x5 grid in Figure 2. Generates p-values for each of the 25 crosses. [1]
6.0 - Cross-direction significance test for selected crosses in Figure 2. Generates p-values for each cross used in cross-direciton test. [1]
7.0 - Individual cross significance test for 5x5 grid in Figure 2. Generates p-values for each of the 50 unique crosses in the grid. [1]
8.0 - Population comparison for reproductive failure rates in Figure 1 (B and C). Generates single p-value for each population comparison. [1]
9.0 - Individual cross significance test for samples in Figure 1 (B and C). Generates p-values for individual crosses used in preliminary scans. [1] 

 Generalied Linear Model
- R scripts for glm used in [1]

 Anova 
- R scripts for anova in [1]

Note: Resampling relies on the pseudo-random number generator module in python ('random'). Due to this, identical inputs to script may produce slightly different output. To force identical outputs for a given input, seed the random generator in script before the first call to the random module (e.g. rd.seed(10)).

# Cited by: 
[1] https://www.biorxiv.org/content/10.1101/2022.10.13.512131v1
