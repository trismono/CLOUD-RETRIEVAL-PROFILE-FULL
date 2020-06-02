#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program for

Created on %(date)

@author : trismonock
@mail   : T.C.Krisna@sron.nl
"""

import numpy as np

def cloud_profile(cloud_file,ztop,zbase,iwc_t,iwc_b,reff_t,reff_b,k):
    # ++++++++++++++++++++
    # define cloud profile
    # ++++++++++++++++++++
    # define n layer
    n_layer = 15
    
    # convert altitude from km to meter
    z_t = ztop*1E3
    z_b = zbase*1E3
    
    # define geometrical thickness
    h = abs(z_t-z_b)
    
    # define layer height
    z = np.linspace(0,h,n_layer-1)
    alt = np.linspace(zbase,ztop,n_layer)
    
    # define constant
    a0 = reff_t+reff_b
    a1 = reff_t**k
    a2 = (reff_t**k)-(reff_b**k)
    
    # define reff : exponential decrease 
    reff_exp_de = a0-(a1-a2*z/h)**(1/k)
    
    # define reff : linear decrease reff
    reff_li = np.linspace(reff_b,reff_t,n_layer-1)
    
    # deviation reff
    reff_dev = reff_li-reff_exp_de
    
    # define reff : final result
    reff = reff_li+reff_dev
        
    # iwc profile : linear decrease
    iwc = np.linspace(iwc_b,iwc_t,n_layer-1)
    
    # create array
    profile = np.zeros(shape=(n_layer,3))
    profile[:,0] = np.flip(alt)
    profile[1:,1] = np.flip(iwc)
    profile[1:,2] = np.flip(reff)

    # ++++++++++++++++
    # create interface
    # ++++++++++++++++    
    # open file
    file = open(cloud_file, "w")
    
    # writing parameter    
    file.write("# z(km)  IWC(g/m3)  r_eff(micron)\n")    
    for i in range(n_layer):                  
        file.write("%7.4f     %6.3f         %6.3f\n" %(profile[i,0], profile[i,1], profile[i,2]))
    
    # close file
    file.close()   
    
    # return output
    return(None)