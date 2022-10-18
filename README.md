Various bootstrap resampling scripts to test for significant differences between population averages. Detailed description of the resampling approaches used in the following scripts can be found in the Materials and Methods section of []. Bootstrap versions include:

5.0 - Combined-cross significance test for 5x5 grid in Figure 2. Generates p-values for each of the 25 crosses.

6.0 - Cross-direction significance test for selected crosses in Figure 2. Generates p-values for each cross used in cross-direciton test.

7.0 - Individual cross significance test for 5x5 grid in Figure 2. Generates p-values for each of the 50 unique crosses in the grid.

8.0 - Population comparison for reproductive failure rates in Figure 1 (B and C). Generates single p-value for each population comparison.

9.0 - Individual cross significance test for samples in Figure 1 (B and C). Generates p-values for individual crosses used in preliminary scans. (Table S2,S3) 

Note: Resampling relies on the pseudo-random number generator module in python ('random'). For identical p-value output, seed random generator in script before the first call to the random module (e.g. random.seed(10)).

For help on input requirements on script, run script without flags ($python bootstrap_5.0.22.py).
