### Grid individual cross pvalues (50 p-values)

import argparse
import random as rd
import numpy as np
import pandas as pd
import itertools as it
from decimal import Decimal

#Seed random generator if equivalant p_values between script runs are desired
#rd.seed(10)

parser = argparse.ArgumentParser(description='P-value Bootstrapper')
parser.add_argument('--i', help='Input File Path', required=True)
parser.add_argument('--wn', help='Within Population Numerator Column Header',required=True)
parser.add_argument('--wd', help='Within Population Denominator Column Header',required=True)
parser.add_argument('--bn', help='Between Population Numerator Column Header',required=True)
parser.add_argument('--bd', help='Between Population Denominator Column Header',required=True)
parser.add_argument('--n', help='number of replicate draws per instance [default: 1000000)',default='1000000',type=int,required=False)
parser.add_argument('--pb', help='Paternal Between Column Header',required=True)
parser.add_argument('--mb', help='Maternal Between Column Header',required=True)
args = parser.parse_args()

df = pd.read_csv(args.i) # Load dataframe

line_m = df[args.mb].dropna().astype(str)
line_p = df[args.pb].dropna().astype(str)
between_nums = df[args.bn].dropna().astype(int)
between_denoms = df[args.bd].dropna().astype(int)
within_nums = df[args.wn].dropna().astype(int)
within_denoms = df[args.wd].dropna().astype(int)
assert len(line_m) == len(line_p) # sanity
assert len(between_nums) == len(between_denoms) # sanity
assert len(within_nums) == len(within_denoms) # sanity
emp_list = list(range(0, len(line_m)))
z = len(within_nums)-1

###
p_value_list = []
for cross in emp_list:
	i=0
	for rep in range(0,args.n):
		j = rd.randint(0, z) # random within cross
		## Resample within using within denom
		num_w = within_nums[j]
		denom_w = within_denoms[j]
		sampler_1 = [0] * (denom_w - num_w)
		sampler_1.extend([1] * num_w)
		assert len(sampler_1) == denom_w # sanity
		choices_1 = rd.choices(sampler_1, k=denom_w)
		num_w2 = int(choices_1.count(1)) # resampled sterile count
		
		## Resample within using between denom
		sampler_2 = [0] * (denom_w - num_w2)
		sampler_2.extend([1] * num_w2)
		assert len(sampler_2) == denom_w # sanity
		k = between_denoms[cross] # current between cross denom
		choices_2 = rd.choices(sampler_2, k=k)
		resample = int(choices_2.count(1))
		
		## Compare resample to empirical count
		if resample >= between_nums[cross]:
			i += 1
	## Calculate p-value
	a = line_m[cross]
	b = line_p[cross]
	p_value = Decimal(float(i/args.n))
	p_value_f = f"{Decimal(float(i/args.n)):.4e}"
	print("cross: " + a + " / " + b)
	print("p-value: " + str(p_value)) #output to stdout
	print("================")
	i=0 # sanity clear		 
