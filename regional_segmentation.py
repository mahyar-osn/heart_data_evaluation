import numpy as np


def OFT():
    return np.linspace(1, 200, 200, dtype=np.int)


def OFT_Dorsal():
    a = np.linspace(1, 25, 25, dtype=np.int)
    b = np.linspace(76, 125, 50, dtype=np.int)
    c = np.linspace(176, 200, 25, dtype=np.int)
    return np.hstack((a, b, c))


def OFT_Ventral():
    a = np.linspace(26, 75, 50, dtype=np.int)
    b = np.linspace(126, 175, 50, dtype=np.int)
    return np.hstack((a, b))


def VNT():
    return np.linspace(201, 600, 400, dtype=np.int)


def VNT_Dorsal():
    a = np.linspace(201, 225, 25, dtype=np.int)
    b = np.linspace(276, 325, 50, dtype=np.int)
    c = np.linspace(376, 425, 50, dtype=np.int)
    d = np.linspace(476, 525, 50, dtype=np.int)
    e = np.linspace(576, 600, 25, dtype=np.int)
    return np.hstack((a, b, c, d, e))


def VNT_Ventral():
    a = np.linspace(226, 275, 50, dtype=np.int)
    b = np.linspace(326, 375, 50, dtype=np.int)
    c = np.linspace(426, 475, 50, dtype=np.int)
    d = np.linspace(526, 575, 50, dtype=np.int)
    return np.hstack((a, b, c, d))


def VNT_Mid_Large():
    return np.linspace(201, 500, 300, dtype=np.int)


def VNT_Mid_Large_Dorsal():
    a = np.linspace(201, 225, 25, dtype=np.int)
    b = np.linspace(276, 325, 50, dtype=np.int)
    c = np.linspace(376, 425, 50, dtype=np.int)
    d = np.linspace(476, 500, 25, dtype=np.int)
    return np.hstack((a, b, c, d))


def VNT_Mid_Large_Ventral():
    a = np.linspace(226, 275, 50, dtype=np.int)
    b = np.linspace(326, 375, 50, dtype=np.int)
    c = np.linspace(426, 475, 50, dtype=np.int)
    return np.hstack((a, b, c))


def VNT_Caudal():
    return np.linspace(501, 600, 100, dtype=np.int)


def VNT_Caudal_Dorsal():
    a = np.linspace(501, 525, 25, dtype=np.int)
    b = np.linspace(576, 600, 25, dtype=np.int)
    return np.hstack((a, b))


def VNT_Caudal_Ventral():
    return np.linspace(526, 575, 50, dtype=np.int)


def VNT_Mid_Small():
    return np.linspace(301, 500, 200, dtype=np.int)


def VNT_Mid_Small_Dorsal():
    a = np.linspace(301, 325, 25, dtype=np.int)
    b = np.linspace(376, 425, 50, dtype=np.int)
    c = np.linspace(476, 500, 25, dtype=np.int)
    return np.hstack((a, b, c))


def VNT_Mid_Small_Ventral():
    a = np.linspace(326, 375, 50, dtype=np.int)
    b = np.linspace(426, 475, 50, dtype=np.int)
    return np.hstack((a, b))


def VNT_Cranial():
    return np.linspace(201, 300, 100, dtype=np.int)


def VNT_Cranial_Dorsal():
    a = np.linspace(201, 225, 25, dtype=np.int)
    b = np.linspace(276, 300, 25, dtype=np.int)
    return np.hstack((a, b))


def VNT_Cranial_Ventral():
    return np.linspace(226, 275, 50, dtype=np.int)


def make_pd_indx(region):
    return np.asarray([x - 1 for x in region], dtype=np.int)
