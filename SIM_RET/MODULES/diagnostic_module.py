#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program for

Created on %(date)

@author : trismonock
@mail   : T.C.Krisna@sron.nl
"""

import numpy as np

def diagnostic(stat_file,pix_id,message,niter,chi2,x,gain_file,lambda_meas,G):    
    # open statistic file
    with open(stat_file, 'w+') as fid:
        # write a header :: variable names and units
        fid.write("%8s%10s%10s%10s%8s%18s%18s%9s\n" %("pix_id",          # pixel idntifier
                                                     "conv_id",          # convergence diagnostic
                                                     "n_iter",           # number of iteration
                                                     "chi2",             # cost function
                                                     "tau",              # tau
                                                     "reff_top (\mu)",   # reff_top
                                                     "reff_base (\mu)",  # reff_base
                                                     "shape_k"))         # shape_parameter
        
        # write retrieval outputs
        fid.write("%8i%10i%10i%10.3f%8.3f%18.3f%18.3f%9.3f" %(pix_id,    # pixel idntifier
                                                             message,    # convergence diagnostic
                                                             niter,      # number of iteration
                                                             chi2,       # cost function
                                                             x[0],       # tau
                                                             x[1],       # reff_top
                                                             x[2],       # reff_base
                                                             x[3]))      # shape_parameter
    
    # create array for gain :: lambda, gain_tau, gain_reff_top, gain_reff_base, gain_shape_parameter 
    data = np.zeros(shape=(len(lambda_meas),5), dtype = float)
    
    # assign data to array
    data[:,0] = lambda_meas     # lambda
    data[:,1:] = G.T            # gain :: original dimension = nstate * n_meas
    
    # write gain matrix into file :: lambda, gain tau, gain reff_top, gain reff_base, gain shape
    np.savetxt(gain_file, data, fmt=["%10.3f", "%20e", "%20e", "%20e", "%20e"])    
    
    
    
    
    
