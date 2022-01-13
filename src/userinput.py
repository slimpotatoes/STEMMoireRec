import numpy as np
import imageio as iio
import ncempy.io as nio

import datastruct as ds


def read_dm3(filename):
    dm3 = nio.read(filename)
    imagedata = verify_data(dm3['data'])
    smh_data = ds.STEMMoireData(imagedata)
    pxunit = verify_pixel_unit(dm3['pixelUnit'])
    pxsize = verify_pixel_size(dm3['pixelSize'])
    if pxsize != None:
        smh_data.pxsize = pxsize * pxunit
    print('dm3 file imported with a pixel spacing of ', smh_data.pxsize , ' pm.')
    return smh_data

def read_emd(filename):
    emd = nio.emd.emdReader(filename)
    #to do
    
def read_image(filename):
    im = iio.read(filename)
    #to do

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

def verify_pixel_size(pxsize):
    if pxsize[0] != pxsize[1]:
        raise ValueError('The pixel spacing is different in both dimensions')
    if isinstance(pxsize[0], (int,float, np.int, np.float, np.int16, np.float16, np.int32, np.float32,
                              np.int64, np.float64)) == False:
        print('The pixel spacing is not recognized as a number, please calibrate the pixel spacing in pm manually')
        return None
    else:
        if pxsize[0] <= 0:
            print('The pixel spacing is not a positive number, please input a proper pixel spacing in pm manually')
            return None
        else:
            return pxsize[0]


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
    return unit_cor

def crystal_info(data, a, b, c, alpha, beta, gamma, sym):
    alpha = np.pi * alpha / 180
    beta = np.pi * beta / 180
    gamma = np.pi * gamma / 180
    data.crystal_info = (a, b, c, alpha, beta, gamma)
    data.crystal_sym = sym
    gamma_star_cos = (np.cos(alpha) * np.cos(beta) - np.cos(gamma)) / (np.sin(alpha) * np.sin(beta))
    gamma_star_sin = 1 - gamma_star_cos ** 2
    data.matrix_crystal_3Dortho = np.matrix([[a * np.sin(beta) * gamma_star_sin, 0 , 0],
                                             [a * np.sin(beta) * gamma_star_cos, b * np.sin(beta) , 0],
                                             [a * np.cos(beta), b * np.cos(beta), c]])
    print(data.matrix_crystal_3Dortho)
    return

def exp_info(data, res, sampling_base):
    data.stem_res = res
    #data.sampling_base = np.array(sampling_base)
    data.sampling_base = np.array([[1/np.sqrt(2), 1/np.sqrt(2), 0], [0, 0, 1], [1/np.sqrt(2), - 1/np.sqrt(2), 0]])
    print(data.sampling_base)
    return