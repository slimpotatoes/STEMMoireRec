import numpy as np

def moire_shift(p, g_c_x, g_c_y):
    '''Provide the Moire shift n_x, n_y for the reflection g_c in the 2D base (b_x, b_y) for the pixel spacing p'''
    if p <= 0:
        ValueError('p <= 0 is not allowed')
    if p > 0:
        n_x = np.floor(g_c_x * p + 1 / 2)
        n_y = np.floor(g_c_y * p + 1 / 2)
        return n_x, n_y
    else:
        ValueError('Inappropriate pixel spacing')


def simulate_moire_sampling(data):
    data.moire_reflections = []
    p = data.pxsize_adjusted
    for reflection in data.crystal_reflections:
        if p <= 0:
            ValueError('p <= 0 is not allowed')
        if p > 0:
            shift = moire_shift(p, reflection['crystal_x'], reflection['crystal_y'])
            data.moire_reflections.append({'moire_x': reflection['crystal_x'] - shift[0] * 1 / p,
                                           'moire_y': reflection['crystal_y'] - shift[1] * 1 / p,
                                           'shift': np.array([shift[0], shift[1]]),
                                           'hkl': reflection['hkl']})
        else:
            ValueError('Inappropriate pixel spacing')
    print('Moire sampling simulation done with the pixel spacing : ', p, ' pm')
    return data.moire_reflections