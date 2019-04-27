import os, sys

import pandas as pd
import numpy as np

import read_write_data as io
import regional_segmentation as rs

from src.analysis import CSV, Plotting, Stats


class Regionalize:
    def __init__(self, data_frame, region_indx):
        self._df = data_frame
        self._indx = region_indx
        self._array_size = region_indx.shape[0]
        self._array = np.zeros((self._array_size, data_frame.shape[1]))
        self._header = list(self._df.columns.values)

    def get_data(self):
        counter = 0
        for i in self._df['Region']:
            if i in self._indx:
                self._array[counter] = self._df[self._df['Region'] == i]
                counter += 1

        return pd.DataFrame(self._array, columns=self._header)


""" A dict for some parameter configuration """
config = dict()
config['root'] = './dataset'
config['subject'] = '53'

config['file_name'] = 'sorted_data.csv'
config['variables'] = ['Cell Number', 'Volume3d']
if config['subject'] == '50':
    config['time'] = 0.25
elif config['subject'] == '59':
    config['time'] = 0.50
if config['subject'] == '52':
    config['time'] = 0.75
if config['subject'] == '53':
    config['time'] = 1.0
config['output_dir'] = '/hpc/mosa004/Nazanin_Heart_fitting/Heart_2/FieldFitting/evaluate/output/img'

""" File name """
filename = os.path.join(config['root'], config['subject'], config['file_name'])

csv = CSV(filename)
plot = Plotting()
stats = Stats()

""" Read the data file into data frame """
df = csv.readCSV(header=0, drop=True, usecols=config['variables'])

""" adding the Time column """
time = np.ones((600,))
time = [x * config['time'] for x in time]
df['Time'] = pd.Series(time, index=df.index)

""" adding the Region column """
region = np.linspace(1, 600, 600, dtype=np.int)
df['Region'] = pd.Series(region, index=df.index)


""" Regionalizing """
oft_indx = rs.OFT()
REG = Regionalize(df, oft_indx)
oft = REG.get_data()


""" Plotiing """
x, y = 'Region', config['variables'][-1]
scatter_img_file = x + '_vs_' + y + '.png'
output_path = os.path.join(config['output_dir'], config['subject'])
if not os.path.exists(output_path):
    os.makedirs(output_path)
output_file = os.path.join(output_path, scatter_img_file)
plot.plotSimpleScatter(x, y, df, save=True, path=output_file)

print('done')



