#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program for

Created on %(date)

@author : trismonock
@mail   : T.C.Krisna@sron.nl
"""

import numpy as np

def uvspec_input(lib_data_dir,cloud_file,input_file,sza,phi0,phi,zout,doy,\
                 albedo_file,lambda0,lambda1,tau550,aerosol_season,aerosol_haze):
    
    # +++++++++++++++++++++++++
    # define standard parameter
    # +++++++++++++++++++++++++
    # standard parameter (change accordingly)
    atm_profile = "afglms"
    source = "solar"
    solar_type = "kurudz_1.0nm"
    rte_solver = "fdisort2"
    mol_abs_parameter = "lowtran"
    umu = np.array([-1.0, 1.0], dtype = float) # default setting = upward and nadir looking
    nstream = 16                    # for better radiance accuracy, increase nstream (number of stream)
    ic_model = "yang2013"           # for ice cloud (consistent with MODIS L2 V6)
    ic_habit = "column_8elements"   # for ice cloud (consistent with MODIS L2 V6)
    ic_rough = "severe"             # for ice cloud (consistent with MODIS L2 V6)

    # +++++++++++++++++
    # create input file
    # +++++++++++++++++
    # open file
    file = open(input_file, "w") 

    # write input parameters       
    file.write("data_files_path " + lib_data_dir +"/\n")
    file.write("atmosphere_file " + lib_data_dir + "/atmmod/" + atm_profile + ".dat\n")
    file.write("source " + source + " " + lib_data_dir + "/solar_flux/" + solar_type + ".dat\n")
    file.write("albedo_file " + albedo_file + "\n")
    file.write("day_of_year " + doy + "\n")
    file.write("sza " + sza + "\n")
    file.write("phi0 " + phi0 + "\n")    
    file.write("phi " + phi + "\n")
    file.write("umu %.1f %.1f\n" %(umu[0], umu[1]))
    file.write("zout " + zout + "\n")
    file.write("rte_solver " + rte_solver + "\n")
    file.write("mol_abs_param " + mol_abs_parameter + "\n")
    file.write("number_of_streams %i\n" %nstream)
    file.write("wavelength "  + lambda0 + " " + lambda1 + "\n")
    file.write("aerosol_default\n")
    file.write("aerosol_haze " + aerosol_haze + "\n")
    file.write("aerosol_season " + aerosol_season + "\n")
    file.write("ic_file 1D " + cloud_file + "\n") 
    file.write("ic_properties " + ic_model + " interpolate\n")
    file.write("ic_habit_" + ic_model + " " + ic_habit + " " + ic_rough + "\n")
    file.write("ic_modify tau550 set " + tau550 + "\n") 	     
    file.write("quiet")      # quiet
#    file.write("verbose")   # print verbose file (useful for post analysis)

    # close file
    file.close()