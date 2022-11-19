# Description

This repository contains scripts used to generate p-values in Lollar et al. 2022[1]. All scripts can be run from personal computers, with one requirement that input file take the format of a comma-separated file (csv) with headers. Headers are required as input flags are mostly header names for dataset categories.

Call script with '--help' flag for information on the input requirement (header names) for each script. 

## Bootstrap versions include:
5.0 - Combined-cross significance test for 5x5 grid in Figure 2. Generates p-values for each of the 25 crosses. [Table ]
6.0 - Cross-direction significance test for selected crosses in Figure 2. Generates p-values for each cross used in cross-direciton test. [Table ]
7.0 - Individual cross significance test for 5x5 grid in Figure 2. Generates p-values for each of the 50 unique crosses in the grid. [Table ]
8.0 - Population comparison for reproductive failure rates in Figure 1 (B and C). Generates single p-value for each population comparison. [Table ]
9.0 - Individual cross significance test for samples in Figure 1 (B and C). Generates p-values for individual crosses used in preliminary scans. [Table S2,S3] 

Note: Resampling relies on the pseudo-random number generator module in python ('random'). Due to this, identical inputs to script may produce slightly different output. To force identical outputs for a given input, seed the random generator in script before the first call to the random module (e.g. rd.seed(10)).

For help on input requirements on script, run script with 'help' flag. ($python bootstrap_5.0.22.py --help).
Scripts have been tested and run on Python versions 3.x.
Required modules: random, argparse, numpy, pandas, itertools, decimal.Decimal

[1] https://www.biorxiv.org/content/10.1101/2022.10.13.512131v1
