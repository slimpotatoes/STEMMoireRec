import numpy as np
import imageio as iio
import ncempy.io as nio

import datastruct as ds


def read_dm3(filename):
    dm3 = nio.read(filename)
    imagedata = verify_data(dm3['data'])
    smh_data = ds.STEMMoireData(imagedata)
    pxunit = verify_pixel_unit(dm3['pixelUnit'])
    pxsize = verify_pixel_unit(dm3['pixelSize'])
    smh_data.pxsize = pxsize * pxunit
    return smh_data

def read_emd(filename):
    emd = nio.emd.emdReader(filename)
    
    
def read_image(filename):
    im = iio.read(filename)


def verify_data(imagedata):
    if imagedata.ndim != 2:
        raise ValueError('the data loaded is not a 2D array')
    else:
        if imagedata.shape[0] != imagedata.shape[1]:
            raise ValueError('STEMMoireRec is currently not working for 2D arrays not having the same size along'
                             ' both directions')
    for value in np.nditer(np.isreal(imagedata)):
        if value is False:
            raise ValueError('The 2D array is not composed of real numbers.')
    return imagedata

def verify_pixel_size(pxise):
    if pxsize[0] != pxsize[1]:
        raise ValueError('The pixel spacing is different in both dimensions')
    if isinstance(pxise, (int,float)) == False:
        print('The pixel spacing is not recognized as a number, please calibrate the pixel spacing in pm manually')
        return None
    else:
        if pxise[0] <= 0:
            print('The pixel spacing is not a positive number, please input a proper pixel spacing in pm manually')
            return None
        else:
            return pxise[0]


def verify_pixel_unit(pxunit):
    if pxunit[0] != pxunit[1]:
        raise ValueError('The unit of the pixel spacing is different in both dimensions')

    if pxunit[0] == 'm':
        unit_cor = 1e12
    elif pxunit[0] == 'mm':
        unit_cor = 1e9
    elif pxunit[0] == 'um':
        unit_cor = 1e6
    elif pxunit[0] == 'nm':
        unit_cor = 1e3
    elif pxunit[0] == 'pm':
        unit_cor = 1
    else:
        raise ValueError('Pixel unit not recognized, please input the pixel spacing pm manually')
    return pxunit[0] * unit_cor