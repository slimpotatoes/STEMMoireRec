import numpy as np
import matplotlib.pyplot as plt
import datastruct

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