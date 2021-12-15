import numpy as np


class STEMMoireData(object):

    def __init__(self, data, pxsize):
        self.data = data
        self.pxsize = pxsize

    def manual_pixel_size(self, pixelsize):
        if isnumeric(pixelsize, (int,float)) == True and pixelsize > 0:
            self.pxsize = pixelsize
            return print('Pixel spacing ', a, ' pm added')
        else:
            raise ValueError('The pixel spacing is not a positive real number')

    