import numpy as np
import imageio as iio
import ncempy.io as nio

import data

def read_dm3(filename):
    dm3 = nio.read(filename)

def read_emd(filename):
    dm3 = nio.emd.emdReader(filename)

def read_image(filename):
    im = iio.read(filename)