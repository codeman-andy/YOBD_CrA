# YOBD_CrA
Repository for the code used during the development of the Master's thesis "Hunting for Brown Dwarfs in Corona Australis".

AstroAlign_and_Astrometry - Performs the image stacking routine for a set of images taken by a detector

Astrometry - Includes functions relevant to the coordinate calibration step which is done using the Astrometry software

Background_Levelling - Performs a simple background levelling routine so the mosaic is more homogeneous throughout

Besançon Prep - A collection of plots of the magnitude vs. errors of each detector, so as to obtain the exponential fit parameters to feed to the Besançon Galaxy Model simulation

CandidateSelection - In this notebook, several specialized cells prepare the catalog for candidate selection. Different cells perform CMD-selection, PM-selection and parallax selection

Candidate_Analysis - A collection of scripts to analyze the produced list of candidates, producing a variety of lists and histograms

Confirmed Members - Script which creates the list of spectroscopically confirmed CrA members from the Gaia eDR3 catalog

Crossmatch - Script with a cross-matching function, a function which stacks similar catalogs in a given folder of your computer, and another function for problem-solving equal column names when matching

FullRed - This script contains the functions for BIAS reduction, flatfield and bad pixel reduction

H-Alpha_Selection - This script performs the extinction estimation, H-Alpha selection and extinction colour map construction of the Subaru catalog

IMF - Performs the random-selection of sources from our IJKs catalog when matched against the Besançon Galaxy Model, providing an estimation of the contamination rate

KARMA_Prep - Here, the SNR plots for different exposure times are created

ParallaxSelec - The function which executes parallax selection

Photometry_Calibration - Script with the photometry calibration functions for the Subaru catalog

Proper_Motions - Performs the proper motions selection of sources inside a K-sigma region or based on the position of previously known spectroscopically confirmed members of the cloud

ReProject - Builds the mosaic image of the Subaru observations. Makes use of the ReProject package present in the re_project.py file

RunPhotometryCalibrationIndividually - Performs photometry on each individual chip, where each cell corresponds to a different detector and at the end collates the different produced catalogs

RunSExtractorPSFEx - Runs the SExtractor + PSFEx routine on the catalogs produced during the RunPhotometryCalibrationIndividually script execution

SExtractor - Functions to perform the SExtractor + PSFex routines

The Quest for Triplicates - Identifies and averages duplicates and triplicates entries in the Subaru catalog

Utility - A compilation of utility functions used in functions of other scripts

clean_cosmics - Cleans the cosmic-rays present in the images. Uses the ncosmics.py file to access the LACosmics code

ds9_region - Creates DS9 regions from entries in a catalog

ext_lambda - Contains the extinction law used to estimate the extinction of the sources

ncosmics - Contains the LACosmics package to be used during the cosmic-ray cleaning routine

re_project - Contains the ReProject package to be used during the mosaicing routine

