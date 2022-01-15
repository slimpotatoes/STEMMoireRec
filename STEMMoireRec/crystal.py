import numpy as np
import math

def list_reflections(data, max_hkl):
    data.allowed_reflections = []
    data.allowed_reflections_sampling_base = []
    data.crystal_reflections = []
    for h in range(-max_hkl, max_hkl):
        for k in range(-max_hkl, max_hkl):
            for l in range(-max_hkl, max_hkl):
                reflection = np.array([h, k, l])
                reflection_proj_3D = project_new_base(reflection, np.linalg.inv(data.matrix_crystal_3Dortho))
                if norm_vector(reflection_proj_3D) < (1 / data.stem_res):
                    if allowed_reflection(data.crystal_sym, h, k, l) == True:
                        #print(reflection, 1 / norm_vector(reflection_proj_3D), data.crystal_info[0] / np.sqrt(h**2 + k **2 + l **2))
                        data.allowed_reflections.append({'vector': reflection_proj_3D, 'hkl': (h, k, l)})
                        #print(data.allowed_reflections[-1])
                        reflection_proj_sampling_base = project_new_base(reflection_proj_3D, np.linalg.inv(np.matrix(np.transpose(data.sampling_base))))
                        data.allowed_reflections_sampling_base.append(
                            {'vector': reflection_proj_sampling_base, 'hkl': (h, k, l)})
                        # print(data.allowed_reflections_sampling_base[-1])
                        # print(reflection_proj_sampling_base[2], reflection_proj_sampling_base[1])
                        if math.isclose(reflection_proj_sampling_base[2], 0, abs_tol=1e-12) == True and (
                                reflection_proj_sampling_base[0] != 0 or reflection_proj_sampling_base[1] != 0):
                            data.crystal_reflections.append({'crystal_x': reflection_proj_sampling_base[0],
                                                             'crystal_y': reflection_proj_sampling_base[1],
                                                             'hkl':(h, k, l)})
    return data.allowed_reflections

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

def matrix_passage(base):
    A = np.array([[np.dot(base[0], np.array([1, 0, 0])), np.dot(base[0], np.array([0, 1, 0])), np.dot(base[0], np.array([0, 0, 1]))],
                  [np.dot(base[1], np.array([1, 0, 0])), np.dot(base[1], np.array([0, 1, 0])), np.dot(base[1], np.array([0, 0, 1]))],
                  [np.dot(base[2], np.array([1, 0, 0])), np.dot(base[2], np.array([0, 1, 0])), np.dot(base[2], np.array([0, 0, 1]))]])
    A = np.transpose(A)
    return np.linalg.inv(np.matrix(A))