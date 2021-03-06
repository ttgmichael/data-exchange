# -*- coding: utf-8 -*-
"""
.. module:: import_tomoPy_ALS.py
   :platform: Unix
   :synopsis: Import ALS TIFF files in data exchange.

Example on how to use the `xtomo_raw`_ module to read ALS raw tomographic data and reconstruct using tomoPy

:Author:
  `Francesco De Carlo <mailto: decarlof@gmail.com>`_

:Organization:
  Argonne National Laboratory, Argonne, IL 60439 USA

:Version: 2014.08.15

.. _xtomo_raw: dataexchange.xtomo.xtomo_importer.html
"""

# tomoPy: https://github.com/tomopy/tomopy
import tomopy 

# Data Exchange: https://github.com/data-exchange/data-exchange
# Data Exchange: https://github.com/data-exchange/data-exchange
import dataexchange

import re

def main():

# sct missing dark and white counters

    file_name = '/local/dataraid/databank/als/20130626_140005_sorghum_dry_400K/20130626_140005_sorghum_dry_400K_0000_.tif'
    dark_file_name = '/local/dataraid/databank/als/20130626_140005_sorghum_dry_400K/20130626_140005_sorghum_dry_400Kdrk_.tif'
    white_file_name = '/local/dataraid/databank/als/20130626_140005_sorghum_dry_400K/20130626_140005_sorghum_dry_400Kbak_.tif'
    log_file = '/local/dataraid/databank/als/20130626_140005_sorghum_dry_400K/20130626_140005_sorghum_dry_400K.sct'

    hdf5_file_name = '/local/dataraid/databank/dataExchange/tmp/ALS_20130626_140005_sorghum_dry_400K.h5'

# sct OK

    file_name = '/local/dataraid/databank/als/20140731_001306_2477A/data/raw/sacarroll/20140731_001306_2477A_x00y08/20140731_001306_2477A_x00y08_0000_.tif'
    dark_file_name = '/local/dataraid/databank/als/20140731_001306_2477A/data/raw/sacarroll/20140731_001306_2477A_x00y08/20140731_001306_2477A_x00y08drk_.tif'
    white_file_name = '/local/dataraid/databank/als/20140731_001306_2477A/data/raw/sacarroll/20140731_001306_2477A_x00y08/20140731_001306_2477A_x00y08bak_.tif'
    log_file = '/local/dataraid/databank/als/20140731_001306_2477A/data/raw/sacarroll/20140731_001306_2477A_x00y08/20140731_001306_2477A_x00y08.sct'
    hdf5_file_name = '/local/dataraid/databank/dataExchange/tmp/ALS_20140731_001306_2477A_x00y08.h5'

    file_name = '/local/dataraid/databank/als/20140411_045212_SF5/20140411_045212_SF5_medium_size_Wheeler_postcut_scan_relaxed_node_0452_0000_.tif'
    dark_file_name = '/local/dataraid/databank/als/20140411_045212_SF5/20140411_045212_SF5_medium_size_Wheeler_postcut_scan_relaxed_node_0452drk_.tif'
    white_file_name = '/local/dataraid/databank/als/20140411_045212_SF5/20140411_045212_SF5_medium_size_Wheeler_postcut_scan_relaxed_node_0452bak_.tif'
    log_file = '/local/dataraid/databank/als/20140411_045212_SF5/20140411_045212_SF5_medium_size_Wheeler_postcut_scan_relaxed_node_0452.sct'
    hdf5_file_name = '/local/dataraid/databank/dataExchange/tmp/ALS_20140411_045212_SF5.h5'

    file_name = '/local/dataraid/databank/als/20140321_094025_wood_aluminum/20140321_094025_wood_aluminum_0000_.tif'
    dark_file_name = '/local/dataraid/databank/als/20140321_094025_wood_aluminum/20140321_094025_wood_aluminumdrk_.tif'
    white_file_name = '/local/dataraid/databank/als/20140321_094025_wood_aluminum/20140321_094025_wood_aluminumbak_.tif'
    log_file = '/local/dataraid/databank/als/20140321_094025_wood_aluminum/20140321_094025_wood_aluminum.sct'
    hdf5_file_name = '/local/dataraid/databank/dataExchange/tmp/ALS_20140321_094025_wood_aluminum.h5'

    file_name = '/local/dataraid/databank/als/20140715_141352_NaCl/20140715_141352_NaCl-15_NaMgF3-85_01475_5x_0000_.tif'
    dark_file_name = '/local/dataraid/databank/als/20140715_141352_NaCl/20140715_141352_NaCl-15_NaMgF3-85_01475_5xdrk_.tif'
    white_file_name = '/local/dataraid/databank/als/20140715_141352_NaCl/20140715_141352_NaCl-15_NaMgF3-85_01475_5xbak_.tif'
    log_file = '/local/dataraid/databank/als/20140715_141352_NaCl/20140715_141352_NaCl-15_NaMgF3-85_01475_5x.sct'
    hdf5_file_name = '/local/dataraid/databank/dataExchange/tmp/ALS_20140715_141352_NaCl.h5'    


    verbose = True

    # Read ALS log file data
    file = open(log_file, 'r')
    for line in file:
        if '-scanner' in line:
            Source = re.sub(r'-scanner ', "", line)
            if verbose: print 'Facility', Source
        
        if '-object' in line:
            Sample = re.sub(r'-object ', "", line)
            if verbose: print 'Sample', Sample
            
        if '-senergy' in line:
            Energy = re.findall(r'\d+.\d+', line)
            if verbose: print 'Energy', Energy[0]
            
        if '-scurrent' in line:
            Current = re.findall(r'\d+.\d+', line)
            if verbose: print 'Current', Current[0]

        if '-nangles' in line:
            Angles = re.findall(r'\d+', line)
            if verbose: print 'Angles', Angles[0]

        if '-num_bright_field' in line:
            WhiteEnd = re.findall(r'\d+', line)

        if '-num_dark_fields' in line:
            DarkEnd = re.findall(r'\d+', line)

    file.close()
    
    dark_start = 0
    dark_end = int(DarkEnd[0])
    dark_step = 1
    white_start = 0
    white_end = int(WhiteEnd[0])
    white_step = 1
    projections_start = 0
    projections_end = int(Angles[0])

    # set to convert slices between slices_start and slices_end
    # if omitted all data set will be converted   
    slices_start = 1445    
    slices_end = 1449  

    # Read raw data
    read = dataexchange.Import()
    data, white, dark, theta = read.xtomo_raw(file_name = file_name,
                                                       projections_start = projections_start,
                                                       projections_end = projections_end,
                                                       slices_start = slices_start,
                                                       slices_end = slices_end,
                                                       white_file_name = white_file_name,
                                                       white_start = white_start,
                                                       white_end = white_end,
                                                       dark_file_name = dark_file_name,
                                                       dark_start = dark_start,
                                                       dark_end = dark_end,
                                                       projections_digits = 4,
                                                       log='INFO'
                                                       )

    # TomoPy xtomo object creation and pipeline of methods.  
    d = tomopy.xtomo_dataset(log='debug')
    d.dataset(data, white, dark, theta)
    d.normalize()
    d.correct_drift()
    #d.optimize_center()
    d.center=1282.5
    d.gridrec()

    # Write to stack of TIFFs.
    write = dataexchange.Export()
    write.xtomo_tiff(data = d.data_recon, output_file = 'tmp/ALS_tiff_2_tomoPy_', axis=0)

if __name__ == "__main__":
    main()

