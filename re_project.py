import numpy as np
import os
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib.pyplot as plt
import scipy.interpolate
import pdb
import copy
from reproject import reproject_interp
from reproject.mosaicking import find_optimal_celestial_wcs,reproject_and_coadd
	
def mosaic(hdus):
	
	wcs_out, shape_out = find_optimal_celestial_wcs(hdus,auto_rotate=True)
	array, footprint = reproject_and_coadd(hdus, wcs_out, shape_out=shape_out,reproject_function=reproject_interp,match_background=True)
	header=hdus[0][0].header
	header.update(wcs_out.to_header())	
	return array, header
	
def main():
	
	path='/home/kmuzic/Astronomy/Students/CrA/stacked/raw/'
	filter='W-S-I+'
	ims=np.asarray([f for f in os.listdir(path+filter) if ('.fits' in f)])

	for i in range(len(ims)): 
		if i == 0: hdus=[fits.open(path+filter+ims[i])]
		else: hdus=hdus+[fits.open(path+filter+ims[i])]
	array, header = mosaic(hdus)
	fits.writeto('CrA_'+filter+'.fits',array,header,overwrite=True)	
	
			
if __name__ == "__main__":
	main()
