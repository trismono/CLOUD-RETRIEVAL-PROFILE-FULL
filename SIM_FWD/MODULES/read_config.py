#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program for

Created on %(date)

@author : trismonock
@mail   : T.C.Krisna@sron.nl
"""

from configparser import ConfigParser

def read_config(config_file):
    # open and parse config file
    config = ConfigParser()
    config.read(config_file)
    
    # geometry
    sza = config['GEOMETRY']['sza']
    phi0 = config['GEOMETRY']['phi0']
    phi = config['GEOMETRY']['phi']
    zout = config['GEOMETRY']['zout']
    doy = config['GEOMETRY']['doy']

    # albedo    
    albedo_file = config['ALBEDO_FILE']['albedo_file']

    # cloud profile    
    ztop = config['CLOUD_PROFILE']['ztop']
    zbase = config['CLOUD_PROFILE']['zbase']
    reff_t = config['CLOUD_PROFILE']['reff_t']
    reff_b = config['CLOUD_PROFILE']['reff_b']
    k = config['CLOUD_PROFILE']['k']
    tau550 = config['CLOUD_PROFILE']['tau550']
    
    # aerosol
    aerosol_season = config['AEROSOL']['aerosol_season']
    aerosol_haze = config['AEROSOL']['aerosol_haze']
    
    # wavelength
    lambda0 = config['WAVELENGTH']['lambda0']
    lambda1 = config['WAVELENGTH']['lambda1']
    
    # return outputs
    return(sza,phi0,phi,zout,doy,albedo_file,ztop,zbase,reff_t,reff_b,k,tau550,\
           aerosol_season,aerosol_haze,lambda0,lambda1)
    