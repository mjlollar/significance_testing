### Population single p-value comparison

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
parser.add_argument('--wh', help='Within Haplotype Column Header', required=True)
parser.add_argument('--mh', help='Between Maternal Haplotype Column Header', required=True)
parser.add_argument('--ph', help='Between Paternal Haplotype Column Header', required=True)
parser.add_argument('--h', help='Haplotype One', required=True)
parser.add_argument('--hh',help='Haplotype Two', required=True)
args = parser.parse_args()

df = pd.read_csv(args.i) # Load dataframe

### Between and Within population counts
num_temp = list(df.loc[(df[args.mh]==args.h) & (df[args.ph]==args.hh), args.bn].astype(int))
num_temp2 = list(df.loc[(df[args.mh]==args.hh) & (df[args.ph]==args.h), args.bn].astype(int))
num_between = num_temp + num_temp2
denom_temp = list(df.loc[(df[args.mh]==args.h) & (df[args.ph]==args.hh), args.bd].astype(int))
denom_temp2 = list(df.loc[(df[args.mh]==args.hh) & (df[args.ph]==args.h), args.bd].astype(int))
denom_between = denom_temp + denom_temp2
num_within = list(df.loc[(df[args.wh]==args.h) | (df[args.wh]==args.hh), args.wn].astype(int))
denom_within = list(df.loc[(df[args.wh]==args.h) | (df[args.wh]==args.hh), args.wd].astype(int))
emp_sterile = sum(num_between)

i = 0
for rep in range(0,args.n):
	count = 0
	for cross in range(0,len(num_between)):
		within_len = len(num_within) - 1
		j = rd.randint(0,within_len) # pick random within cross by list position

		## Resample within using within denominator
		sampler_1 = [0] * (denom_within[j] - num_within[j])
		sampler_1.extend([1] * num_within[j])
		assert len(sampler_1) == denom_within[j] #sanity
		choices_1 = rd.choices(sampler_1, k=denom_within[j])
		num_within_new = int(choices_1.count(1))
		
		## Resample using between denominator
		sampler_2 = [0] * (denom_within[j] - num_within_new)
		sampler_2.extend([1] * num_within_new)
		assert len(sampler_2) == denom_within[j] #sanity
		choices_2 = rd.choices(sampler_2, k=denom_between[cross])
		resample = int(choices_2.count(1)) # resample count
		count += resample # add count to within resample total

	## Compare within and empirical counts for permutation
	if count >= emp_sterile:
		i += 1
	count = 0 # sanity clear

### Output for Stdout
p_value = Decimal(float(i / args.n))
p_value_f = f"{Decimal(float(i / args.n)):.4e}"
print("Population 1: " + str(args.h))
print("Population 2: " + str(args.hh))
print("P-value: " + str(p_value))
print("P-value (approx.): " + p_value_f)