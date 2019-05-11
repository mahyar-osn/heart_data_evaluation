import os
import pickle

import pandas as pd
import numpy as np
from scipy import stats

from statsmodels.multivariate.manova import MANOVA
from statsmodels.genmod.generalized_linear_model import GLM
import statsmodels.api as sm
from statsmodels.formula.api import ols

# from sklearn.cluster import KMeans
# import matplotlib.pyplot as plt

import sys
sys.path.append('/hpc/mosa004/Lung/Haris_Paper/basic_stats_and_plotting')
from src.analysis import CSV, Plotting
from regional_segmentation import get_regions

# pl = Plotting()


def setup_data():
    """ A dict for some parameter configuration """
    config = dict()
    config['root'] = './dataset'
    config['file_name'] = 'full_data.csv'
    # config['variables'] = ['CellNumber', 'Volume3d', 'Time', 'Region']
    config['variables'] = ['Element', 'Bin', 'CellNumber', 'Anisotropy', 'Area3d', 'Elongation', 'EqDiameter',
                           'FeretShape3d', 'Length3d', 'Orientation2Phi', 'Orientation2Theta', 'OrientationPhi',
                           'OrientationTheta', 'Perimeter', 'Shape_VA3d', 'Volume3d', 'Width3d', 'Time', 'Region']
    config['output_dir'] = '/hpc/mosa004/Nazanin_Heart_fitting/Heart_2/FieldFitting/evaluate/output/img'

    """ File name """
    filename = os.path.join(config['root'], config['file_name'])

    csv = CSV(filename)

    """ Read the data file into data frame """
    df = csv.readCSV(header=0, drop=True, usecols=config['variables'])

    return df, config
    # return config


def write_pickle(d, f):
    """ Get heart regions """
    region_dict = get_regions(d)
    with open(f, "wb") as output_file:
        pickle.dump(region_dict, output_file)


def read_pickle(f):
    with open(f, "rb") as input_file:
        region_dict = pickle.load(input_file)
    return region_dict


def make_region_column(r_dict, r_name):
    region = r_name
    data = r_dict[region]
    data['Region Name'] = pd.Series([region] * data.shape[0], index=data.index)
    return data


def combine_data(d_list):
    return pd.concat(d_list)


def get_timewise_data(d):
    data_timewise = dict()
    data_timewise['T1'] = d[d['Time'] == 0.25]
    data_timewise['T2'] = d[d['Time'] == 0.5]
    data_timewise['T3'] = d[d['Time'] == 0.75]
    data_timewise['T4'] = d[d['Time'] == 1.]
    return data_timewise


def preapare_result_dir(x, y, config, extra_string=None):
    if extra_string is None:
        scatter_img_file = x + '_vs_' + y + '.png'
    else:
        scatter_img_file = x + '_vs_' + y + '_' + extra_string + '.png'
    output_path = os.path.join(config['output_dir'])
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    output_file = os.path.join(output_path, scatter_img_file)
    return output_file


class Statistics:

    def __init__(self):
        pass

    @staticmethod
    def ind_ttest(d1, d2, ev=False):
        """
        Calculate the T-test for the means of two independent samples of scores.

        This is a two-sided test for the null hypothesis that 2 independent samples have identical average (expected)
        values. This test assumes that the populations have identical variances by default.

        :param d1: first data
        :param d2: second data
        :param ev: equal variance (default False) if True perform a standard independent 2 sample test that assumes
        equal population variances.
        :return: t, p
        """

        t, p = stats.ttest_ind(d1, d2, equal_var=ev)

        return t, p

    @staticmethod
    def multivariateLinearRegression(X, y, data, save=False, path=None, useSklearn=False):
        """

        :param X:
        :param y:
        :param data:
        :param save:
        :param path:
        :param useSklearn:
        :return:
        """

        X, Y = np.asarray(data[X]), np.asarray(data[y])
        # X = X.reshape(-1, 1)

        #  remove row if NaN
        # X, Y = X[~np.isnan(X).reshape(-1, 1).any(axis=1)], Y[~np.isnan(Y).reshape(-1, 1).any(axis=1)]

        X = sm.add_constant(X)
        est = sm.OLS(Y, X).fit()
        print(est.summary())


class Plot:

    def __init__(self, x, y, data, hue=None):
        self._x = x
        self._y = y
        self._data = data
        self._hue = hue

    def box(self, palette=None, save=False, path=None):
        pl.plotBox(self._x, self._y, self._hue, self._data, palette, save, path)

    def scatter(self, save=False, path=None):
        pl.plotSimpleScatter(self._x, self._y, self._data, save=save, path=path)

    def scatterCategorical(self, hue_order, size, save=False, path=None):
        pl.plotScatterWithCategorical(self._x, self._y, self._hue, hue_order, size, self._data, save=save, path=path)


if __name__ == '__main__':
    stat = Statistics()

    """ Preparation """
    x, y = 'Time', 'CellNumber'
    hue = 'Region Name'

    df, config = setup_data()
    dfname = './dataset/pickle_dataset/full_data.pkl'
    write_pickle(df, dfname)
    region_dict = read_pickle(dfname)

    data_dorsal = make_region_column(region_dict, 'Dorsal_Point')
    data_ventral = make_region_column(region_dict, 'Ventral_Point')
    data_oft = make_region_column(region_dict, 'OFT')
    data_caudal = make_region_column(region_dict, 'VNT_Caudal')
    full_data = combine_data([data_dorsal, data_ventral, data_oft, data_caudal])

    # if x is "CellNumber" or y is "CellNumber":
    #     pass
    # else:
    #     data_dorsal = data_dorsal[(data_dorsal != 0).all()]
    #     data_ventral = data_ventral[(data_ventral.T != 0).all()]
    #     data_oft = data_oft[(data_oft.T != 0).all()]
    #     data_caudal = data_caudal[(data_caudal.T != 0).all()]
    #     full_data = full_data[(full_data.T != 0).all()]

    # data_dorsal = data_dorsal[(data_dorsal.T != 0).all()]
    # data_ventral = data_ventral[(data_ventral.T != 0).all()]
    # data_oft = data_oft[(data_oft.T != 0).all()]
    # data_caudal = data_caudal[(data_caudal.T != 0).all()]
    full_data = full_data[(full_data.CellNumber != 0)]

    d_dorsal_timewise = get_timewise_data(data_dorsal)
    d_ventral_timewise = get_timewise_data(data_ventral)
    d_oft_timewise = get_timewise_data(data_oft)
    d_caudal_timewise = get_timewise_data(data_caudal)
    full_timewise = get_timewise_data(full_data)

    X = ['Region', 'Time']
    y = ['Orientation2Phi']
    stat.multivariateLinearRegression(X, y, full_timewise)


    """ Statistics """
    # t, p = stat.ind_ttest(d_caudal_timewise['T1']['CellNumber'], d_oft_timewise['T1']['CellNumber'])
    # print("T = ", t, "| ", "P = ", p)
    # t, p = stat.ind_ttest(d_caudal_timewise['T2']['CellNumber'], d_oft_timewise['T2']['CellNumber'])
    # print("T = ", t, "| ", "P = ", p)
    # t, p = stat.ind_ttest(d_caudal_timewise['T3']['CellNumber'], d_oft_timewise['T3']['CellNumber'])
    # print("T = ", t, "| ", "P = ", p)
    # t, p = stat.ind_ttest(d_caudal_timewise['T4']['CellNumber'], d_oft_timewise['T4']['CellNumber'])
    # print("T = ", t, "| ", "P = ", p)

    """ Plotting """
    # t1 = combine_data([d_dorsal_timewise['T3'], d_ventral_timewise['T3'], d_oft_timewise['T3'], d_caudal_timewise['T3']])
    plot = Plot(x, y, full_data, hue=None)

    # output_img = preapare_result_dir(x, y, config, 'box')
    # plot.box(["m", "g", "b", "r"], save=True, path=output_img)
    # output_img = preapare_result_dir(x, y, config, 'scatter_t3')
    # plot.scatter(save=True, path=output_img)
    output_img = preapare_result_dir(x, y, config, 'scatter_category')
    # size = full_data['Volume3d'] *1000
    plot.scatterCategorical(None, size='Volume3d', save=True, path=output_img)


    print('done')

""" Kmeans & Manova (TEMP) """
# X = df[['CellNumber', 'Volume3d']].to_numpy()
# kmeans = KMeans(n_clusters=4)
# kmeans.fit(X)
# y_kmeans = kmeans.predict(X)
# plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
# centres = kmeans.cluster_centers_
# plt.scatter(centres[:, 0], centres[:, 1], c='black', s=200, alpha=0.5)

# indpnd = df[['Time', 'Region']].to_numpy()

# manova = MANOVA(depnd, indpnd)
# manova.fit()

