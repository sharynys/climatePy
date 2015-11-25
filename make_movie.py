#!/usr/bin/env python


import sys
import numpy as np
import argparse

import matplotlib.pyplot as plt
from matplotlib import animation

import netCDF4 as nc

# Comments: script makes a fluid animation using NetCDF data

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('input_file',help="Input file containing data") 
	parser.add_argument('field', help="data field to animate")

	args = parser.parse_args()

# open the input file nb vorticity has dimensions time, dpth, lat long
	f = nc.Dataset(args.input_file)
	
#	with nc.Dataset(args.input_file) as f:
	vorticity = f.variables['vorticity_z']
	vorticity = vorticity[:]
	fig = plt.figure()
	images = []
	
	m = len(f.variables['Time'])
#	print "max" + str(m)

	for t in range(0, m):
		img = plt.imshow(vorticity[t, 0, :, :])
		images.append([img])
		plt.savefig('v' + str(t).zfill(3) + '.png') 
	ani = animation.ArtistAnimation(fig, images, interval=20)
	plt.show()


# temp code for debug
#	import pdb
#	pdb.set_trace()

#close the input file

	f.close()

#	print "ahah"
	return True

if __name__ == "__main__":
	sys.exit(main())
