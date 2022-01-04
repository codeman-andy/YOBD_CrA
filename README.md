# YOBD_CrA
Repository for the code used during the development of the Master's thesis "Hunting for Brown Dwarfs in Corona Australis".

AstroAlign_and_Astrometry - Performs the image stacking routine for a set of images taken by a detector

Astrometry - Includes functions relevant to the coordinate calibration step which is done using the Astrometry software

Background_Levelling - Performs a simple background levelling routine so the mosaic is more homogeneous throughout

CandidateSelection - In this notebook, several specialized cells prepare the catalog for candidate selection. Different cells perform CMD-selection, PM-selection and parallax selection

Crossmatch - Script with a cross-matching function, a function which stacks similar catalogs in a given folder of your computer, and another function for problem-solving equal column names when matching

FullRed - This script contains the functions for BIAS reduction, flatfield and bad pixel reduction

H-Alpha_Selection - This script performs the extinction estimation, H-Alpha selection and extinction colour map construction of the Subaru catalog

KARMA_Prep - Here, the SNR plots for different exposure times are created

ParallaxSelec - The function which executes parallax selection

Photometry_Calibration - Script with the photometry calibration functions for the Subaru catalog

ReProject - Builds the mosaic image of the Subaru observations. Makes use of the ReProject package present in the re_project.py file

SExtractor - Functions to perform the SExtractor + PSFex routines

The Quest for Triplicates - Identifies and averages duplicates and triplicates entries in the Subaru catalog

Utility - A compilation of utility functions used in functions of other scripts

clean_cosmics - Cleans the cosmic-rays present in the images. Uses the ncosmics.py file to access the LACosmics code

ds9_region - Creates DS9 regions from entries in a catalog

ncosmics - Containts the LACosmics package to be used during the cosmic-ray cleaning routine

re_project - Contains the ReProject package to be used during the mosaicing routine

