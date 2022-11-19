### Individual p-values for combined cross, 5x5 grid

import argparse
import random as rd
import numpy as np
import pandas as pd
import itertools as it
from decimal import Decimal

#Seed random generator if equivalant p_values between script runs are desired
#rd.seed(10)

### Inputs (run '--help' for descriptions)
parser = argparse.ArgumentParser(description='P-value Bootstrapper')
parser.add_argument('--i', help='Input File Path', required=True)
parser.add_argument('--wn', help='Within Population Numerator Column Header',required=True)
parser.add_argument('--wd', help='Within Population Denominator Column Header',required=True)
parser.add_argument('--bn', help='Between Population Numerator Column Header',required=True)
parser.add_argument('--bd', help='Between Population Denominator Column Header',required=True)
parser.add_argument('--n', help='number of replicate draws per instance [default: 1000000)',default='1000000',type=int,required=False)
parser.add_argument('--pw', help='Paternal Within Column Header',required=True)
parser.add_argument('--mw', help='Maternal Within Column Header',required=True)
parser.add_argument('--pb', help='Paternal Between Column Header',required=True)
parser.add_argument('--mb', help='Maternal Between Column Header',required=True)
parser.add_argument('--wh', help='Within Maternal Haplotype Column Header', required=True)
parser.add_argument('--bh', help='Between Maternal Haplotype Column Header', required=True)
parser.add_argument('--h', help='Haplotype One', required=True)
parser.add_argument('--hh',help='Haplotype Two', required=True)
args = parser.parse_args()

df = pd.read_csv(args.i) # Load dataframe

## Get within haplotype IDs
wh_one = pd.unique(df.loc[df[args.wh] == args.h, args.mw]).astype(int)
wh_two = pd.unique(df.loc[df[args.wh] == args.hh, args.mw]).astype(int)
wh_comb = np.concatenate([wh_one,wh_two])

## Between haplotype IDs and cross list
bh_one = pd.unique(df.loc[df[args.bh] == args.h, args.mb]).astype(int).tolist()
bh_two = pd.unique(df.loc[df[args.bh] == args.hh, args.mb]).astype(int).tolist()
between_crosses = list(it.product(bh_one, bh_two)) # List of tuples of all crosses

p_value_list = []
### Generate p-values for individual crosses, directions combined (25 p-values in 5x5 grid)
for x,y in between_crosses:
	i = 0
	between_num_1 = df.loc[(df[args.mb]==x) & (df[args.pb]==y), args.bn].squeeze().astype(int)
	between_num_2 = df.loc[(df[args.mb]==y) & (df[args.pb]==x), args.bn].squeeze().astype(int)
	denom_b1 = df.loc[(df[args.mb]==x) & (df[args.pb]==y), args.bd].squeeze().astype(int) # between numerator 1
	denom_b2 = df.loc[(df[args.mb]==y) & (df[args.pb]==x), args.bd].squeeze().astype(int) # between numerator 2
	empirical_sterile = between_num_1 + between_num_2 # Get empirical total for cross
	for rep in range(0,args.n):
		## Pick random within population cross
		line_one_w = rd.choice(wh_comb) # Random line in grid, one_w is considered 
		if line_one_w in wh_one:
			waldo = np.where(wh_one == line_one_w)
			new_one = np.delete(wh_one, waldo)
			line_two_w = rd.choice(new_one)
		else:
			waldo = np.where(wh_two == line_one_w)
			new_one = np.delete(wh_two, waldo)
			line_two_w = rd.choice(new_one)
		
		## Resample within crosses using within cross denominators
		num_w1 = df.loc[(df[args.mw]==line_one_w) & (df[args.pw]==line_two_w), args.wn].squeeze().astype(int) # within numerator 1
		num_w2 = df.loc[(df[args.mw]==line_two_w) & (df[args.pw]==line_one_w), args.wn].squeeze().astype(int) # within numerator 2 (cross direction partner)
		denom_w1 = df.loc[(df[args.mw]==line_one_w) & (df[args.pw]==line_two_w), args.wd].squeeze().astype(int) # within denominator 1
		denom_w2 = df.loc[(df[args.mw]==line_two_w) & (df[args.pw]==line_one_w), args.wd].squeeze().astype(int) # within denominator 2
		
		# Resample within cross 1
		sampler_1 = [0] * (denom_w1 - num_w1) # "0" = fertile
		sampler_1.extend([1] * num_w1) # "1" = sterile
		assert len(sampler_1) == denom_w1 # sanity
		choices_1 = rd.choices(sampler_1, k=denom_w1) # resample with replacement
		num_w1 = int(choices_1.count(1)) # count steriles

		# Resample within cross 2
		sampler_2 = [0] * (denom_w2 - num_w2) 
		sampler_2.extend([1] * num_w2)
		assert len(sampler_2) == denom_w2 # sanity
		choices_2 = rd.choices(sampler_2, k=denom_w2)
		num_w2 = int(choices_2.count(1))
		
		## Resample from within direction 1 & 2 cross number equal to between denom 1/2, repectively.
		sampler_3 = [0] * (denom_w1 - num_w1)
		sampler_3.extend([1] * num_w1)
		sampler_4 = [0] * (denom_w2 - num_w2)
		sampler_4.extend([1] * num_w2)
		resample_w1 = rd.choices(sampler_3, k=denom_b1)
		resample_w2 = rd.choices(sampler_4, k=denom_b2)
		resample_total = int(resample_w1.count(1)) + int(resample_w2.count(1))
		if resample_total >= empirical_sterile:
			i += 1
	
	p_value = Decimal(float(i / args.n))
	p_value_f = f"{Decimal(float(i / args.n)):.4e}"
	p_value_list.append(p_value)
	print("cross: " + str(x) + ' / ' + str(y))
	print("p_value: " + str(p_value)) #output pvalue to terminal
	print("p_value (approx): " + p_value_f)
	print("=======")
	i = 0 # sanity clear	
