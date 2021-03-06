# -*- coding: utf-8 -*-
"""
.. module:: import_tomoPy_Australian.py
   :platform: Unix
   :synopsis: import Australian Synchrotron Facility TIFF files in data exchange.

Example on how to use the `xtomo_raw`_ module to read Australian Synchrotron Facility TIFF raw tomographic data and reconstruct with tomoPy

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
import dataexchange

def main():
    # read a series of tiff
    file_name = '/local/dataraid/databank/AS/Mayo_tooth_AS/SAMPLE_T_.tif'
    dark_file_name = '/local/dataraid/databank/AS/Mayo_tooth_AS/DF__BEFORE_.tif'
    white_file_name = '/local/dataraid/databank/AS/Mayo_tooth_AS/BG__BEFORE_.tif'

    sample_name = 'Teeth'

    projections_start = 0
    projections_end = 1801
    white_start = 0
    white_end = 10
    white_step = 1
    dark_start = 0
    dark_end = 10
    dark_step = 1

    # to reconstruct slices from slices_start to slices_end
    # if omitted all data set is recontructed
    slices_start = 290    
    slices_end = 294    

    # Read raw data
    read = dataexchange.Import()
    data, white, dark, theta = read.xtomo_raw(file_name,
                                                       projections_start = projections_start,
                                                       projections_end = projections_end,
                                                       slices_start = slices_start,
                                                       slices_end = slices_end,
                                                       white_file_name = white_file_name,
                                                       white_start = white_start,
                                                       white_end = white_end,
                                                       white_step = white_step,
                                                       dark_file_name = dark_file_name,
                                                       dark_start = dark_start,
                                                       dark_end = dark_end,
                                                       dark_step = dark_step,
                                                       projections_digits = 4,
                                                       white_digits = 2,
                                                       dark_digits = 2,
                                                       projections_zeros = True,
                                                       log='INFO'
                                                    )    

    # TomoPy xtomo object creation and pipeline of methods.  
    d = tomopy.xtomo_dataset(log='debug')
    d.dataset(data, white, dark, theta)
    d.normalize()
    d.correct_drift()
    #d.optimize_center()
    #d.phase_retrieval()
    #d.correct_drift()
    d.center=1184.0
    d.gridrec()

    # Write to stack of TIFFs.
    write = dataexchange.Export()
    write.xtomo_tiff(data = d.data_recon, output_file = 'tmp/Australian_tiff_2_tomoPy_', axis=0)

if __name__ == "__main__":
    main()

