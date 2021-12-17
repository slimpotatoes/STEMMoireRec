import numpy as np

def list_reflections(data, max_hkl):
    for h in range(-max_hkl, max_hkl):
        for k in range(-max_hkl, max_hkl):
            for l in range(-max_hkl, max_hkl):
                reflection = np.array([h, k, l])
                reflection_proj_3D = project_new_base(reflection, np.linalg.inv(np.matrix(data.matrix_crystal_3Dortho)))
                if norm_vector(reflection_proj_3D) < (1 / data.stem_res):
                    if allowed_reflection(data.crystal_sym, h, k, l) == True:
                        #print(reflection, 1 / norm_vector(reflection_proj_3D), data.crystal_info[0] / np.sqrt(h**2 + k **2 + l **2))
                        data.list_allowed_reflections.append({'vector': reflection_proj_3D, 'hkl': (h, k, l)})
    return data.list_allowed_reflections

def allowed_reflection(sym, h, k, l):
    if sym == 'FCC':
        if h % 2 == k % 2 and h % 2 == l % 2:
            return True
        else:
            return False

def project_new_base(reflection, matrix_change_base):
    reflection_adapt = np.swapaxes(np.array([reflection]), 0, 1)
    reflection_new = np.asarray(np.swapaxes(np.matmul(matrix_change_base, reflection_adapt), 0, 1)).ravel()
    return reflection_new

def norm_vector(reflection):
    return np.sqrt(reflection[0]**2 + reflection[1]**2 + reflection[2]**2)