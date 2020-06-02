#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program for

Created on %(date)

@author : trismonock
@mail   : T.C.Krisna@sron.nl
"""

import numpy as np

def kmat_module(input_file1,input_file2,input_file3,input_file4,input_file5,tau1,tau2,\
                reff_t1,reff_t2,reff_b1,reff_b2,k1,k2,lambda_meas,rad_meas,sy,outfile):
    
    # open and read data
    data_ref = np.loadtxt(input_file1, skiprows=1)
    data_ptau = np.loadtxt(input_file2, skiprows=1)
    data_preff_t = np.loadtxt(input_file3, skiprows=1)
    data_preff_b = np.loadtxt(input_file4, skiprows=1)
    data_pk = np.loadtxt(input_file5, skiprows=1)
    
    # parse data : 0 = lambda, 1 = irradiance down, 2 = radiance up
    rad_up_ref = data_ref[:,2]
    rad_up_ptau = data_ptau[:,2]
    rad_up_preff_t = data_preff_t[:,2]
    rad_up_preff_b = data_preff_b[:,2]
    rad_up_pk = data_pk[:,2]
    
    # define dimension
    nspectra = len(rad_up_ref)
    
    # define dimension column
    ncol = 8                # wavelength, spectra_meas, sy, spectra_mod, kmat_tau, kmat_reff_top, kmat_reff_base, k
    
    # create array
    kmat_array =  np.zeros(shape=(nspectra,ncol))  
        
    # calculate jacobian tau and reff
    kmat_tau = (rad_up_ref-rad_up_ptau)/(tau1-tau2)
    kmat_reff_t = (rad_up_ref-rad_up_preff_t)/(reff_t1-reff_t2)
    kmat_reff_b = (rad_up_ref-rad_up_preff_b)/(reff_b1-reff_b2)
    kmat_k = (rad_up_ref-rad_up_pk)/(k1-k2)

    # assign data to array
    kmat_array[:,0] = lambda_meas
    kmat_array[:,1] = rad_meas
    kmat_array[:,2] = sy
    kmat_array[:,3] = rad_up_ref
    kmat_array[:,4] = kmat_tau
    kmat_array[:,5] = kmat_reff_t
    kmat_array[:,6] = kmat_reff_b
    kmat_array[:,7] = kmat_k
    
    # save kmat output
    np.savetxt(outfile, kmat_array, fmt=["%10.3f", "%20e", "%20e", "%20e", "%20e", "%20e", "%20e", "%20e"])
    
    # return output
    return(kmat_array)