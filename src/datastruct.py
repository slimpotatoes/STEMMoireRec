import numpy as np


class STEMMoireData(object):

    def __init__(self):
        self.data = None
        self.pxsize = None

    def manual_pixel_size(self, a):
        self.pxsize = a 
        return print('Pixel spacing ', a, ' pm added')
    