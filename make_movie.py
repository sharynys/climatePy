#!/usr/bin/env python

import sys
import numpy as np
import argparse
import netCDF4 as nc

# Comments: script makes a fluid animation using NetCDF data

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('input_file',help="Input file containing data") 
	parser.add_argument('field', help="data field to animate")

	args = parser.parse_args()
	print "ahah"
	return True

if __name__ == "__main__":
	sys.exit(main())
