# -*- coding: utf-8 -*-
"""
.. module:: convert_SRC.py
   :platform: Unix
   :synopsis: Convert Synchrotron Radiation Center DPT files in data exchange.

Example on how to use the `xtomo_raw`_ module to read Synchrotron Radiation Center Infrared raw tomographic data and save them as Data Exchange

:Author:
  `Francesco De Carlo <mailto: decarlof@gmail.com>`_

:Organization:
  Argonne National Laboratory, Argonne, IL 60439 USA

:Version: 2014.08.15

.. _xtomo_raw: dataexchange.xtomo.xtomo_importer.html
"""

# Data Exchange: https://github.com/data-exchange/data-exchange
import dataexchange

def main():

    raw_tiff_base_name = "/local/dataraid/databank/dataExchange/microCT/SRC/raw/FPA_16_18_18_TOMO_243_Fiber_2500_50_50_"    
    hdf5_base_name = "/local/dataraid/databank/dataExchange/tmp/SRC_"    
   
    log_file = raw_tiff_base_name + "wavelength.dpt"
    angle_file = raw_tiff_base_name + "angle.dpt"

    # Determine projection angle end    
    file = open(angle_file, 'r')
    lines = file.readlines()
    projections_angle_end = float(lines[0]) + float(lines[1])
    file.close()

    file = open(log_file, 'r')
    for line in file:
        linelist = line.split(",")

        file_name = raw_tiff_base_name+linelist[0]+"cm-1.dpt"
        sample_name = raw_tiff_base_name+linelist[0]+"cm-1"

        hdf5_file_name = hdf5_base_name+linelist[0]+"cm-1.h5"

    	# Read raw data
    	read = dataexchange.Import()
    	data, white, dark, theta = read.xtomo_raw(file_name,
                                                        data_type='dpt',
                                                        projections_angle_end = projections_angle_end,
                                                        log='INFO'
                                                        )

    	# Save data as dataExchange
    	write = dataexchange.Export()
    	write.xtomo_exchange(data = data,
                            data_white = white,
                            data_dark = dark,
                            theta = theta,
                            hdf5_file_name = hdf5_file_name,
                            sample_name = sample_name,
                            data_exchange_type = 'tomography_raw_projections'
                            )
    file.close()

if __name__ == "__main__":
    main()

