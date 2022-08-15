### Cross-direction test for selected crosses in 5x5 grid

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
parser.add_argument('--a', help='Line one', required=True, type=int)
parser.add_argument('--b', help='Line two', required=True, type=int)
parser.add_argument('--c', help='Line one header', required=True)
parser.add_argument('--d', help='Line two header', required=True)
parser.add_argument('--s', help='Sterile count header', required=True)
parser.add_argument('--t', help='Total count header', required=True)
parser.add_argument('--n', help='Permutation replicates [default=1000000]', required=False, default='1000000', type=int)
parser.add_argument('--mh', help='Maternal Hapltype of empirical cross', required=True, choices=['FR', 'ZI'])
args = parser.parse_args()

df = pd.read_csv(args.i) # Load dataframe

if args.mh == 'FR':	
	emp_sterile = df.loc[(df[args.c]==args.a) & (df[args.d]==args.b), args.s].squeeze().astype(int)
	emp_total = df.loc[(df[args.c]==args.a) & (df[args.d]==args.b), args.t].squeeze().astype(int)
	con_sterile = df.loc[(df[args.c]==args.b) & (df[args.d]==args.a), args.s].squeeze().astype(int)
	con_total = df.loc[(df[args.c]==args.b) & (df[args.d]==args.a), args.t].squeeze().astype(int)
else:
	emp_sterile = df.loc[(df[args.c]==args.b) & (df[args.d]==args.a), args.s].squeeze().astype(int)
	emp_total = df.loc[(df[args.c]==args.b) & (df[args.d]==args.a), args.t].squeeze().astype(int)
	con_sterile = df.loc[(df[args.c]==args.a) & (df[args.d]==args.b), args.s].squeeze().astype(int)
	con_total = df.loc[(df[args.c]==args.a) & (df[args.d]==args.b), args.t].squeeze().astype(int)
	
print(emp_sterile)
print(emp_total)
print(con_sterile)	
print(con_total)

i = 0
for rep in range(0,args.n):
	## Resample control direction using within denominator
	sampler = [0] * (con_total - con_sterile)
	sampler.extend([1] * con_sterile)
	assert len(sampler) == con_total # sanity
	choices = rd.choices(sampler, k=con_total)
	
	## Resample control direction using empirical denominator:
	resample = rd.choices(sampler, k=emp_total)
	resample_count = int(resample.count(1))
	if resample_count >= emp_sterile:
		i += 1

### Print to stdout
p_value = Decimal(float(i / args.n))
p_value_f = f"{Decimal(float(i / args.n)):.4e}"
print("cross: " + str(args.a) + ' / ' + str(args.b))
print("p_value: " + str(p_value)) #output pvalue to terminal
print("p_value (approx): " + p_value_f)



		
