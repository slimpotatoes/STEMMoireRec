import numpy as np
import imageio as iio
import ncempy.io as nio

import datastructure as ds

def read_dm3(filename):
    dm3 = nio.read(filename)

    if dm3['data'].ndim !=2:
        raise ValueError('the data loaded is not a 2D array')
    else:
        smh_data = ds.STEMMoireData()

        if dm3['pixelUnit'] == '':
            print('Image not calibrated, please input the pixel spacing manually')
            smh_data.data = dm3['data']
        elif dm3['pixelUnit'] == 'nm':
            smh_data.data = dm3['data']
            smh_data.pxsize = dm3['pizelSize']



    return smh_data

def read_emd(filename):
    dm3 = nio.emd.emdReader(filename)
    
    
def read_image(filename):
    im = iio.read(filename)

def verify_data(imagedata, pxspacing, pxunit):
    if