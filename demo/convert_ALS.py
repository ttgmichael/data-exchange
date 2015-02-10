# -*- coding: utf-8 -*-
"""
.. module:: convert_ALS.py
   :platform: Unix
   :synopsis: Convert ALS TIFF files in data exchange.

Example on how to use the `xtomo_raw`_ module to read ALS raw tomographic data and save them as Data Exchange

:Author:
  `Francesco De Carlo <mailto: decarlof@gmail.com>`_

:Organization:
  Argonne National Laboratory, Argonne, IL 60439 USA

:Version: 2014.08.15

.. _xtomo_raw: dataexchange.xtomo.xtomo_importer.html
"""

# Data Exchange: https://github.com/data-exchange/data-exchange
import dataexchange
import h5py
import re

def find_dataset(name):
    """ Find first object with '20150130_065956_AX1_Jan15_x00y00' anywhere in the file """
    if '20150130_065956_AX1_Jan15_x00y00' in name:
        return name

def main():

# sct missing dark and white counters

    #file_name = '/local/dataraid/databank/als/20130626_140005_sorghum_dry_400K/20130626_140005_sorghum_dry_400K_0000_.tif'
    #dark_file_name = '/local/dataraid/databank/als/20130626_140005_sorghum_dry_400K/20130626_140005_sorghum_dry_400Kdrk_.tif'
    #white_file_name = '/local/dataraid/databank/als/20130626_140005_sorghum_dry_400K/20130626_140005_sorghum_dry_400Kbak_.tif'
    #log_file = '/local/dataraid/databank/als/20130626_140005_sorghum_dry_400K/20130626_140005_sorghum_dry_400K.sct'

    #hdf5_file_name = '/local/dataraid/databank/dataExchange/tmp/ALS_20130626_140005_sorghum_dry_400K.h5'

# sct OK

    #file_name = '/local/dataraid/databank/als/20140731_001306_2477A/data/raw/sacarroll/20140731_001306_2477A_x00y08/20140731_001306_2477A_x00y08_0000_.tif'
    #dark_file_name = '/local/dataraid/databank/als/20140731_001306_2477A/data/raw/sacarroll/20140731_001306_2477A_x00y08/20140731_001306_2477A_x00y08drk_.tif'
    #white_file_name = '/local/dataraid/databank/als/20140731_001306_2477A/data/raw/sacarroll/20140731_001306_2477A_x00y08/20140731_001306_2477A_x00y08bak_.tif'
    #log_file = '/local/dataraid/databank/als/20140731_001306_2477A/data/raw/sacarroll/20140731_001306_2477A_x00y08/20140731_001306_2477A_x00y08.sct'
    #hdf5_file_name = '/local/dataraid/databank/dataExchange/tmp/ALS_20140731_001306_2477A_x00y08.h5'

    #file_name = '/local/dataraid/databank/als/20140411_045212_SF5/20140411_045212_SF5_medium_size_Wheeler_postcut_scan_relaxed_node_0452_0000_.tif'
    #dark_file_name = '/local/dataraid/databank/als/20140411_045212_SF5/20140411_045212_SF5_medium_size_Wheeler_postcut_scan_relaxed_node_0452drk_.tif'
    #white_file_name = '/local/dataraid/databank/als/20140411_045212_SF5/20140411_045212_SF5_medium_size_Wheeler_postcut_scan_relaxed_node_0452bak_.tif'
    #log_file = '/local/dataraid/databank/als/20140411_045212_SF5/20140411_045212_SF5_medium_size_Wheeler_postcut_scan_relaxed_node_0452.sct'
    #hdf5_file_name = '/local/dataraid/databank/dataExchange/tmp/ALS_20140411_045212_SF5.h5'

    #file_name = '/local/dataraid/databank/als/20140321_094025_wood_aluminum/20140321_094025_wood_aluminum_0000_.tif'
    #dark_file_name = '/local/dataraid/databank/als/20140321_094025_wood_aluminum/20140321_094025_wood_aluminumdrk_.tif'
    #white_file_name = '/local/dataraid/databank/als/20140321_094025_wood_aluminum/20140321_094025_wood_aluminumbak_.tif'
    #log_file = '/local/dataraid/databank/als/20140321_094025_wood_aluminum/20140321_094025_wood_aluminum.sct'
    #hdf5_file_name = '/local/dataraid/databank/dataExchange/tmp/ALS_20140321_094025_wood_aluminum.h5'

    file_name = '/cygdrive/s/mttang/PluginDatasetsTest/20150130_065956_AX1_Jan15_x00y00.h5'
    dark_file_name = '20150130_065956_AX1_Jan15_x00y00drk_'
    white_file_name = '20150130_065956_AX1_Jan15_x00y00bak_'
    #sct_file = '/cygdrive/s/mttang/PluginDatasetsTest/20141112_132339_AmmoniteFossil/20141112_132339_AmmoniteFossil.sct'

    # for validate to work
    hdf5_file_name = '/cygdrive/c/tomopy-masterWindows/demo/eclipse/EXCHANGE2.h5'

    verbose = True

    # Read ALS log file data
#    file = open(sct_file, 'r')
#    for line in file:
#        if '-scanner' in line:
#            Source = re.sub(r'-scanner ', "", line)
#            if verbose: print 'Facility', Source
#        
#        if '-object' in line:
#            Sample = re.sub(r'-object ', "", line)
#            if verbose: print 'Sample', Sample
#            
#        if '-senergy' in line:
#            Energy = re.findall(r'\d+.\d+', line)
#            if verbose: print 'Energy', Energy[0]
#            
#        if '-scurrent' in line:
#            Current = re.findall(r'\d+.\d+', line)
#            if verbose: print 'Current', Current[0]
#
#        if '-nangles' in line:
#            Angles = re.findall(r'\d+', line)
#            if verbose: print 'Angles', Angles[0]
#
#        if '-num_bright_field' in line:
#            WhiteEnd = re.findall(r'\d+', line)
#            if verbose: print 'WhiteEnd', WhiteEnd[0]
#
#        if '-num_dark_fields' in line:
#            DarkEnd = re.findall(r'\d+', line)
#            if verbose: print 'DarkEnd', DarkEnd[0]

    with h5py.File(file_name, 'r') as f:
                   
        dset = f[f.visit(find_dataset)]
        
        dsetname = f.visit(find_dataset)
        print dsetname
        
        for keys in dset.attrs.keys():
            #print keys + ":", dset.attrs[keys]
            if 'scanner' in keys:
                Source = dset.attrs[keys]
                if verbose: print 'Facility', Source
            
            if 'object' in keys:
                Sample = dset.attrs[keys]
                if verbose: print 'Sample', Sample
            
            if 'senergy' in keys:
                Energy = dset.attrs[keys]
                if verbose: print 'Energy', Energy
            
            if 'scurrent' in keys:
                Current = dset.attrs[keys]
                if verbose: print 'Current', Current
                    
            if 'nangles' in keys:
                Angles = dset.attrs[keys]
                if verbose: print 'Angles', Angles          
                  
            if 'num_bright_field' in keys:
                WhiteEnd = dset.attrs[keys]
                if verbose: print 'WhiteEnd', WhiteEnd
                
            if 'num_dark_fields' in keys:
                DarkEnd = dset.attrs[keys]
                if verbose: print 'DarkEnd', DarkEnd

    f.close()
    
    dark_start = 0
    dark_end = int(DarkEnd)
    dark_step = 1
    white_start = 0
    white_end = int(WhiteEnd)
    white_step = 1
    projections_start = 0
    projections_end = int(Angles)

    print dark_end, white_end, projections_end

    file_name = file_name + "&" + dsetname

    # Read raw data
    read = dataexchange.Import()
    data, white, dark, theta = read.xtomo_raw(file_name = file_name,
                                                       projections_start = projections_start,
                                                       projections_end = projections_end,
                                                       white_file_name = white_file_name,
                                                       white_start = white_start,
                                                       white_end = white_end,
                                                       dark_file_name = dark_file_name,
                                                       dark_start = dark_start,
                                                       dark_end = dark_end,
                                                       projections_digits = 4,
                                                       data_type = 'als_hdf5',
                                                       log='INFO'
                                                       )


    # Save data as dataExchange
    write = dataexchange.Export()
    write.xtomo_exchange(data = data,
                          data_white = white,
                          data_dark = dark,
                          theta = theta,
                          hdf5_file_name = hdf5_file_name,
                          sample_name = Sample,
                          data_exchange_type = 'tomography_raw_projections'
                          )


if __name__ == "__main__":
    main()

