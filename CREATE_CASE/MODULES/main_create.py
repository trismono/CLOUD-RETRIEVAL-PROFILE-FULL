#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program for

Created on %(date)

@author : trismonock
@mail   : T.C.Krisna@sron.nl
"""

# import modules
import os

# limit the number of cores
os.environ["OPENBLAS_NUM_THREADS"] = "3"      # limit the number of thread

import numpy as np
from config_module import config_module
import itertools

# get and define the working directory
base_dir = os.getcwd() + "/"
os.chdir(base_dir)

# define dirs
data_dir = os.path.realpath(base_dir + "../../DATA") + "/" 
out_dir = os.path.realpath(base_dir + "../OUTPUT") + "/" 

# create dir
try:
    os.makedirs(out_dir)
except OSError:
    pass

# +++++++++++++++++
# measurement setup
# +++++++++++++++++
sza = 30.0
phi0 = 100.0
phi = 0
zout = 10.0
doy = 85    				# day of year
albedo_file = data_dir + "albedo_sea_water.dat"
ztop = 9.0
zbase = 8.0
tau550 = np.array([0.3,0.6,1.2])  	# optical thickness
reff_t = np.array([8,10,12])     	# effective radius cloud top (micron)
reff_b = np.array([20,30,40])   	# effectice radius cloud base (micron)
k = np.array([3,4,5])               	# shape parameter
aerosol_haze = "4"
aerosol_season = "1"
lambda0 = 400
lambda1 = 2000

# ++++++++++++++++++
# create combination
# ++++++++++++++++++
comb = itertools.product(tau550,reff_t,reff_b,k)
comb = np.array(list(comb))

# ++++++++++++
# create cases
# ++++++++++++
# define dimension
nobs = len(comb)

# loop overr pixels
for i in range(nobs):
    # print statement
    print("Info    | Generating case pixel id :", i+1)

    # define filename
    outfile = out_dir + "meas_setup_%i.dat" %(i+1)
    
    # call config module
    config_module(filename=outfile,sza=sza,phi0=phi0,phi=phi,zout=zout,doy=doy,\
                  albedo_file=albedo_file,ztop=ztop,zbase=zbase,tau550=comb[i,0],\
                      reff_t=comb[i,1],reff_b=comb[i,2],k=comb[i,3],\
                          aerosol_season=aerosol_season,aerosol_haze=aerosol_haze,\
                              lambda0=lambda0,lambda1=lambda1)
