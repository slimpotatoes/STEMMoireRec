import numpy as np


class STEMMoireData(object):

    def __init__(self, data, pxsize=None):
        self.data = data
        self.pxsize = None
        self.pxsize_adjust = None
        self.crystal_info = None
        self.stem_res = None
        self.matrix_crystal_3Dortho = None
        self.sampling_base = None
        self.crystal_sym = None
        self.allowed_reflections = []
        self.allowed_reflections_sampling_base = []
        self.crystal_reflections = []
        self.moire_reflections = []
        self.masks = []
        self.masks_param = []
        self.reconstruction = []

    def manual_pixel_size(self, pixelsize):
        if isnumeric(pixelsize, (int,float)) == True and pixelsize > 0:
            self.pxsize = pixelsize
            return print('Pixel spacing ', a, ' pm added')
        else:
            raise ValueError('The pixel spacing is not a positive real number')

    