import numpy as np
import pandas as pd


class Regionalize:
    def __init__(self, data_frame, region_indx):
        self._df = data_frame
        self._indx = region_indx
        self._array_size = region_indx.shape[0] * 4
        self._array = np.zeros((self._array_size, data_frame.shape[1]))
        self._header = list(self._df.columns.values)

    def get_data(self):
        counter = 0
        for region in self._indx:
            self._array[counter:counter + 4] = self._df[self._df['Region'] == region]
            counter += 4
        return pd.DataFrame(self._array, columns=self._header)


def get_regions(df):

    region_dict = dict()

    # OFT
    indx = OFT()
    REG = Regionalize(df, indx)
    region_dict['OFT'] = REG.get_data()
    del indx, REG
    # Ventral_Point
    indx = Ventral_Point()
    REG = Regionalize(df, indx)
    region_dict['Ventral_Point'] = REG.get_data()
    del indx, REG
    # Dorsal_Point
    indx = Dorsal_Point()
    REG = Regionalize(df, indx)
    region_dict['Dorsal_Point'] = REG.get_data()
    del indx, REG
    # VNT_Caudal
    indx = VNT_Caudal()
    REG = Regionalize(df, indx)
    region_dict['VNT_Caudal'] = REG.get_data()

    # # OFT_Dorsal
    # indx = OFT_Dorsal()
    # REG = Regionalize(df, indx)
    # region_dict['OFT_Dorsal'] = REG.get_data()
    # del indx, REG
    # # OFT_Ventral
    # indx = OFT_Ventral()
    # REG = Regionalize(df, indx)
    # region_dict['OFT_Ventral'] = REG.get_data()
    # del indx, REG
    # # VNT
    # indx = VNT()
    # REG = Regionalize(df, indx)
    # region_dict['VNT'] = REG.get_data()
    # del indx, REG
    # # VNT_Dorsal
    # indx = VNT_Dorsal()
    # REG = Regionalize(df, indx)
    # region_dict['VNT_Dorsal'] = REG.get_data()
    # del indx, REG
    # # VNT_Dorsal
    # indx = VNT_Dorsal()
    # REG = Regionalize(df, indx)
    # region_dict['VNT_Dorsal'] = REG.get_data()
    # del indx, REG
    # # VNT_Mid_Large
    # indx = VNT_Mid_Large()
    # REG = Regionalize(df, indx)
    # region_dict['VNT_Mid_Large'] = REG.get_data()
    # del indx, REG
    # # VNT_Mid_Large_Dorsal
    # indx = VNT_Mid_Large_Dorsal()
    # REG = Regionalize(df, indx)
    # region_dict['VNT_Mid_Large_Dorsal'] = REG.get_data()
    # del indx, REG
    # # VNT_Mid_Large_Ventral
    # indx = VNT_Mid_Large_Ventral()
    # REG = Regionalize(df, indx)
    # region_dict['VNT_Mid_Large_Ventral'] = REG.get_data()
    # del indx, REG
    # # VNT_Caudal_Dorsal
    # indx = VNT_Caudal_Dorsal()
    # REG = Regionalize(df, indx)
    # region_dict['VNT_Caudal_Dorsal'] = REG.get_data()
    # del indx, REG
    # # VNT_Caudal_Ventral
    # indx = VNT_Caudal_Ventral()
    # REG = Regionalize(df, indx)
    # region_dict['VNT_Caudal_Ventral'] = REG.get_data()
    # del indx, REG
    # # VNT_Mid_Small
    # indx = VNT_Mid_Small()
    # REG = Regionalize(df, indx)
    # region_dict['VNT_Mid_Small'] = REG.get_data()
    # del indx, REG
    # # VNT_Mid_Small_Dorsal
    # indx = VNT_Mid_Small_Dorsal()
    # REG = Regionalize(df, indx)
    # region_dict['VNT_Mid_Small_Dorsal'] = REG.get_data()
    # del indx, REG
    # # VNT_Mid_Small_Ventral
    # indx = VNT_Mid_Small_Ventral()
    # REG = Regionalize(df, indx)
    # region_dict['VNT_Mid_Small_Ventral'] = REG.get_data()
    # del indx, REG
    # # VNT_Cranial
    # indx = VNT_Cranial()
    # REG = Regionalize(df, indx)
    # region_dict['VNT_Cranial'] = REG.get_data()
    # del indx, REG
    # # VNT_Cranial_Dorsal
    # indx = VNT_Cranial_Dorsal()
    # REG = Regionalize(df, indx)
    # region_dict['VNT_Cranial_Dorsal'] = REG.get_data()
    # del indx, REG
    # # VNT_Cranial_Ventral
    # indx = VNT_Cranial_Ventral()
    # REG = Regionalize(df, indx)
    # region_dict['VNT_Cranial_Ventral'] = REG.get_data()
    # del indx, REG
    # # VNT_Mid_Small_2_Dorsal
    # indx = VNT_Mid_Small_2_Dorsal()
    # REG = Regionalize(df, indx)
    # region_dict['VNT_Mid_Small_2_Dorsal'] = REG.get_data()
    # del indx, REG
    # # VNT_Mid_Small_2_Ventral
    # indx = VNT_Mid_Small_2_Ventral()
    # REG = Regionalize(df, indx)
    # region_dict['VNT_Mid_Small_2_Ventral'] = REG.get_data()
    # del indx, REG

    return region_dict


def OFT():
    return np.linspace(1, 200, 200, dtype=np.int)


def Ventral_Point():
    # return np.asarray([239, 240, 244, 245, 249, 250, 261, 262, 263, 266, 267, 268, 271, 272, 273, 329, 330, 334,
    #                    335, 351, 352, 356, 357, 361, 362], dtype=np.int)
    return np.asarray([239, 240, 244, 245, 249, 250, 261, 262, 266, 267, 271, 272, 329, 330, 334,
                       335, 339, 340, 344, 345, 349, 350, 351, 352, 356, 357, 361, 362, 366, 367, 370, 371, 429, 430,
                       434, 435, 451, 452, 456, 457], dtype=np.int)


def Dorsal_Point():
    return np.asarray([201, 202, 206, 207, 211, 212, 216, 217, 221, 222, 279, 280, 284, 285, 289, 290, 294, 295,
                       299, 300, 301, 302, 306, 307, 311, 312, 316, 317, 321, 322, 379, 380, 384, 385, 389, 390,
                       394, 395, 399, 400, 401, 402, 406, 407, 479, 480, 484, 485], dtype=np.int)


def VNT_Caudal():
    return np.linspace(501, 600, 100, dtype=np.int)



# def OFT_Dorsal():
#     a = np.linspace(1, 25, 25, dtype=np.int)
#     b = np.linspace(76, 125, 50, dtype=np.int)
#     c = np.linspace(176, 200, 25, dtype=np.int)
#     return np.hstack((a, b, c))
#
#
# def OFT_Ventral():
#     a = np.linspace(26, 75, 50, dtype=np.int)
#     b = np.linspace(126, 175, 50, dtype=np.int)
#     return np.hstack((a, b))
#
#
# def VNT():
#     return np.linspace(201, 600, 400, dtype=np.int)
#
#
# def VNT_Dorsal():
#     a = np.linspace(201, 225, 25, dtype=np.int)
#     b = np.linspace(276, 325, 50, dtype=np.int)
#     c = np.linspace(376, 425, 50, dtype=np.int)
#     d = np.linspace(476, 525, 50, dtype=np.int)
#     e = np.linspace(576, 600, 25, dtype=np.int)
#     return np.hstack((a, b, c, d, e))
#
#
# def VNT_Ventral():
#     a = np.linspace(226, 275, 50, dtype=np.int)
#     b = np.linspace(326, 375, 50, dtype=np.int)
#     c = np.linspace(426, 475, 50, dtype=np.int)
#     d = np.linspace(526, 575, 50, dtype=np.int)
#     return np.hstack((a, b, c, d))
#
#
# def VNT_Mid_Large():
#     return np.linspace(201, 500, 300, dtype=np.int)
#
#
# def VNT_Mid_Large_Dorsal():
#     a = np.linspace(201, 225, 25, dtype=np.int)
#     b = np.linspace(276, 325, 50, dtype=np.int)
#     c = np.linspace(376, 425, 50, dtype=np.int)
#     d = np.linspace(476, 500, 25, dtype=np.int)
#     return np.hstack((a, b, c, d))
#
#
# def VNT_Mid_Large_Ventral():
#     a = np.linspace(226, 275, 50, dtype=np.int)
#     b = np.linspace(326, 375, 50, dtype=np.int)
#     c = np.linspace(426, 475, 50, dtype=np.int)
#     return np.hstack((a, b, c))
#
#
# def VNT_Caudal_Dorsal():
#     a = np.linspace(501, 525, 25, dtype=np.int)
#     b = np.linspace(576, 600, 25, dtype=np.int)
#     return np.hstack((a, b))
#
#
# def VNT_Caudal_Ventral():
#     return np.linspace(526, 575, 50, dtype=np.int)
#
#
# def VNT_Mid_Small():
#     return np.linspace(301, 500, 200, dtype=np.int)
#
#
# def VNT_Mid_Small_Dorsal():
#     a = np.linspace(301, 325, 25, dtype=np.int)
#     b = np.linspace(376, 425, 50, dtype=np.int)
#     c = np.linspace(476, 500, 25, dtype=np.int)
#     return np.hstack((a, b, c))
#
#
# def VNT_Mid_Small_Ventral():
#     a = np.linspace(326, 375, 50, dtype=np.int)
#     b = np.linspace(426, 475, 50, dtype=np.int)
#     return np.hstack((a, b))
#
#
# def VNT_Cranial():
#     return np.linspace(201, 300, 100, dtype=np.int)
#
#
# def VNT_Cranial_Dorsal():
#     a = np.linspace(201, 225, 25, dtype=np.int)
#     b = np.linspace(276, 300, 25, dtype=np.int)
#     return np.hstack((a, b))
#
#
# def VNT_Cranial_Ventral():
#     return np.linspace(226, 275, 50, dtype=np.int)
#
#
# def VNT_Mid_Small_2_Dorsal():
#     a = np.linspace(201, 225, 25, dtype=np.int)
#     b = np.linspace(276, 325, 50, dtype=np.int)
#     c = np.linspace(376, 400, 25, dtype=np.int)
#     return np.hstack((a, b, c))
#
#
# def VNT_Mid_Small_2_Ventral():
#     a = np.linspace(226, 275, 50, dtype=np.int)
#     b = np.linspace(326, 375, 50, dtype=np.int)
#     return np.hstack((a, b))



def make_pd_indx(region):
    return np.asarray([x - 1 for x in region], dtype=np.int)
