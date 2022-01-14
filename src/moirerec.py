import numpy as np

def mask_gaussian(center, r, shape):
    """Return the mask function in the image space I defined by shape (see MIS). The Gaussian mask takes the center of a
        circle center = (xc,yc) and its radius r to generate a 2D gaussian function centered around the circle. In
        addition, the center of the mask is used to return g_0 that correspond to the unstrained reference."""
    """Do not forget event coordinate (x,y) from matplotlib  should be switched compared to numpy array indexing"""
    g_0 = np.array([(center[1] - 0.5 * shape[0]) / shape[0] * np.ones(shape),
                    (center[0] - 0.5 * shape[1]) / shape[1] * np.ones(shape)])
    """Do not forget event coordinate (x,y) from matplotlib  should be switched compared to numpy array indexing
    - r corresponds  to 3 * sigma => 99% gaussian mask included in circle"""
    const = 1 / (2 * (r / 3) ** 2)
    mesh_x, mesh_y = np.meshgrid(np.arange(shape[0]), np.arange(shape[1]))
    delta_x = (mesh_x - center[0]) ** 2
    delta_y = (mesh_y - center[1]) ** 2
    mask = np.exp(-(delta_x + delta_y) * const)
    return mask

def masking_moire_ft(center_r, reflection_r, data):
    moire_ft_masked = np.zeros(np.shape(data.data), dtype=np.complex128)
    mask_center = mask_gaussian((np.shape(data.data)[0] / 2, np.shape(data.data)[1] / 2), center_r, np.shape(data.data))
    moire_ft_masked_center = np.multiply(np.fft.fftshift(np.fft.fft2(data.data)), mask_center)
    moire_ft_masked = np.add(moire_ft_masked_center, moire_ft_masked)
    data.masks.append({'hkl' : (0, 0, 0), 'mask_x' : np.shape(data.data)[0] / 2 , 'mask_y' : np.shape(data.data)[1] / 2,
                       'mask_radius' : center_r, 'moire_ft_masked': moire_ft_masked_center, 'shift' : np.array([0, 0])})

    for reflection in data.moire_reflections:
        mask_x = reflection['moire_x'] * np.shape(data.data)[0]/2 * (2 * data.pxsize) + np.shape(data.data)[0]/2
        mask_y = -(reflection['moire_y'] * np.shape(data.data)[1]/2 * (2 * data.pxsize) - np.shape(data.data)[1]/2)
        mask = mask_gaussian([mask_x, mask_y], reflection_r, np.shape(data.data))
        moire_ft_masked_reflection = np.multiply(np.fft.fftshift(np.fft.fft2(data.data)), mask)
        moire_ft_masked = np.add(moire_ft_masked_reflection, moire_ft_masked)
        data.masks.append({'hkl': reflection['hkl'], 'mask_x': mask_x, 'mask_y': mask_y, 'mask_radius': reflection_r,
                           'moire_ft_masked': moire_ft_masked_reflection, 'shift' : reflection['shift']})
        print(reflection['hkl'], mask_x, mask_y)
    return moire_ft_masked

def moire_reconstruction(data, tiles):
    rec_image_fft = np.zeros((tiles * np.shape(data.data)[0], tiles * np.shape(data.data)[1]), dtype=np.complex128)
    print(np.shape(rec_image_fft))
    for mask in data.masks:
        rec_temp = np.zeros((tiles * np.shape(data.data)[0], tiles * np.shape(data.data)[1]), dtype=np.complex128)
        index_x_0 = np.shape(rec_image_fft)[0] / 2 - mask['shift'][1] * np.shape(data.data)[0] - np.shape(data.data)[0] / 2
        index_x_1 = np.shape(rec_image_fft)[0] / 2 - mask['shift'][1] * np.shape(data.data)[0] + np.shape(data.data)[0] / 2
        index_y_0 = np.shape(rec_image_fft)[1] / 2 + mask['shift'][0] * np.shape(data.data)[1] - np.shape(data.data)[1] / 2
        index_y_1 = np.shape(rec_image_fft)[1] / 2 + mask['shift'][0] * np.shape(data.data)[1] + np.shape(data.data)[1] / 2
        data.reconstruction.append({'hkl': mask['hkl'],
                                    'y': np.shape(rec_image_fft)[1] / 2 - mask['shift'][1] * np.shape(data.data)[1]
                                         + mask['mask_y'] - np.shape(data.data)[1] / 2,
                                    'x': np.shape(rec_image_fft)[0] / 2 + mask['shift'][0] * np.shape(data.data)[0]
                                         + mask['mask_x'] - np.shape(data.data)[0] / 2})

        '''print('x : ', int(index_x_0), int(index_x_1))
        print('y : ', int(index_y_0), int(index_y_1))

        print(np.shape(rec_temp[int(index_x_0):int(index_x_1), int(index_y_0):int(index_y_1)]))
        print(np.shape(mask['moire_ft_masked']))'''

        rec_temp[int(index_x_0):int(index_x_1), int(index_y_0):int(index_y_1)] = mask['moire_ft_masked']
        rec_image_fft = np.add(rec_image_fft, rec_temp)
    rec_image = np.fft.ifft2(np.fft.ifftshift(rec_image_fft))
    return rec_image