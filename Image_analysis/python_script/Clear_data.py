# -------------------------------------------------------------------------------------- #
# EPFL Bachelor Project : Testing and verification of a tape-spring based solar array    #
# Authors:                                                                               #
# Cédric Fontaine                                                                        #
# Jérémie Arthur Maurice Pochon                                                          #
# Malicia Leipold                                                                        #
# Tony Govoni                                                                            #
# April 18.04.2020                                                                       #
# -------------------------------------------------------------------------------------- #

# Python image tracking and analysis 2020
# Code developer :
# Tony Govoni
#_________________________________________

#Clear_data : The goal of this script is to clear all past data from an older record
#_________________________________________

#importing module
import os
#_________________________________________

# 1. Creating all the different path

path_to_dir  = 'data'  # path to directory to clean

path_to_dir2  = 'data_contour'  # path to directory to clean number 2

path_to_dir3  = 'data/binary'  # path to directory to clean number 3

files_in_dir = os.listdir(path_to_dir)# get list of files in the directory

files_in_dir2 = os.listdir(path_to_dir2)#

files_in_dir3 = os.listdir(path_to_dir3)#

# 2. Cleaning loop
for file in files_in_dir: #we loop all files in a directoy
    if file !='binary':#save binary file
        os.remove(f'{path_to_dir}/{file}')# delete file
for file in files_in_dir2:
    os.remove(f'{path_to_dir2}/{file}')# delete file
for file in files_in_dir3:
    if (file !='My_data') and (file !='Settings'):#save My_data file and Settings
        os.remove(f'{path_to_dir3}/{file}')# delete file

print("\nclear all done")

# end
# -------------------------------------------------------------------------------------- #
