import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import datastruct

plt.style.use('dark_background')

def imview(image, cmap='gray', vmin=None, vmax=None):
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111)
    ax.imshow(image, cmap=cmap, vmin=vmin, vmax=vmax)
    plt.show()
    return

def imview_fft(image, cmap='gray', vmin=None, vmax=None):
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111)
    fft_image = np.log10(np.abs(np.fft.fftshift(np.fft.fft2(image))))
    ax.imshow(fft_image, cmap=cmap, vmin=vmin, vmax=vmax)
    plt.show()
    return

def imview_sim(data):
    Cref_x = []
    Cref_y = []
    Mref_x = []
    Mref_y = []
    p = data.pxsize
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111)
    SMH_Gamma = Rectangle((-1/(2*p), -1/(2*p)), 1/p, 1/p, fill=False, color='green')
    for Cref in data.crystal_reflections:
        ax.annotate(Cref['hkl'], (Cref['crystal_x'], Cref['crystal_y']))
        Cref_x.append(Cref['crystal_x'])
        Cref_y.append(Cref['crystal_y'])
    for Mref in data.moire_reflections:
        ax.annotate(Mref['hkl'], (Mref['moire_x'], Mref['moire_y']))
        Mref_x.append(Mref['moire_x'])
        Mref_y.append(Mref['moire_y'])
    ax.scatter(Cref_x, Cref_y, c='b', alpha = 1)
    ax.scatter(Mref_x, Mref_y, c='r', alpha = 0.5)
    ax.add_artist(SMH_Gamma)
    plt.show()
    return