import numpy as np
import imageio as iio
import ncempy.io as nio

import datastruct as ds


def read_dm3(filename):
    dm3 = nio.read(filename)
    imagedata, pxsize = verify_data(dm3['data'], dm3['pixelSize'], dm3['pixelUnit'])
    data = ds.STEMMoireData()

    return smh_data

def read_emd(filename):
    emd = nio.emd.emdReader(filename)
    
    
def read_image(filename):
    im = iio.read(filename)


def verify_data(imagedata, pxsize, pxunit):
    if imagedata.ndim != 2:
        raise ValueError('the data loaded is not a 2D array')
    else:
        if imagedata.shape[0] != imagedata.shape[1]:
            raise ValueError('STEMMoireRec is currently not working for 2D arrays not having the same size along'
                             ' both directions')

    for value in np.nditer(np.isreal(imagedata)):
        if value is False:
            raise ValueError('The 2D array is not composed of real numbers.')

    if pxsize[0] != pxsize[1]:
        raise ValueError('The pixel spacing is different in both dimensions')

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
        raise ValueError('Pixel unit not recognized, please input the pixel spacing manually')

    if verify_pixel_size(pxsize[0]) is True:
        pxsize_final = pxsize[0] * unit_cor
    else:
        pxsize_final = None
        raise ValueError('The pixel spacing must be a strictly positive real number')
    return imagedata, pxsize_final


def verify_pixel_size(pxise):
    if isinstance(pxise, (int,float)) == False:
        raise ValueError('The pixel size is not a number')
    else:
        if pxise <= 0:
            return False
        else:
            return True

