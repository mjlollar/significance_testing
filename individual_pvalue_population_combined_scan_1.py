### This script used to generate single p-values for population pair scans

import argparse
import random as rd
from decimal import Decimal

parser = argparse.ArgumentParser(description='Generate botstrap p-values for individual crosses in population group assays')
parser.add_argument('--wn', help='Total within population numerator (sum of six crosses)', required=True, type=int)
parser.add_argument('--wd', help='Total within population denominator (sum of 6 crosses)', required=True, type=int)
parser.add_argument('--bn', help='Between population cross numerator', required=True, type=int)
parser.add_argument('--bd', help='Between population cross denominator', required=True, type=int)
parser.add_argument('--n', help='Number of permutations to perform (default=1000000)', required=False, default=1000000)
args = parser.parse_args()

i=0
for rep in range(0, args.n): ### for each permutation replicate
	### Generate sampling list from within group
	sampler_1 = [0] * (args.wd - args.wn)
	sampler_1.extend([1] * args.wn)
	assert len(sampler_1) == args.wd #Sanity
	choices_1 = rd.choices(sampler_1, k=args.wd) #Resample within using within denominator
	within_num = int(choices_1.count(1)) # new within sterile count

	sampler_2 = [0] * (args.wd - within_num)
	sampler_2.extend([1] * within_num)
	assert len(sampler_2) == args.wd #Sanity
	choices_2 = rd.choices(sampler_2, k=args.bd) # Resample within using between denominator
	resample = int(choices_2.count(1))
	
	if resample >= args.bn:
		i += 1

## Caluclate and print P-value
p_value = Decimal(float(i/args.n))
p_value_f = f"{Decimal(float(i/args.n)):.4e}"
print("P-value: " + str(p_value))
print("P-value (approx.): " + p_value_f)
