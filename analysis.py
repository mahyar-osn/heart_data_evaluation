import os, sys

import pandas as pd
import numpy as np

import read_write_data as io

from src.analysis import CSV, Plotting, Stats

from regional_segmentation import get_regions


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


""" Get heart regions """
regions = get_regions(df)


""" Plotiing """
x, y = 'Region', config['variables'][-1]
scatter_img_file = x + '_vs_' + y + '.png'
output_path = os.path.join(config['output_dir'], config['subject'])
if not os.path.exists(output_path):
    os.makedirs(output_path)
output_file = os.path.join(output_path, scatter_img_file)
plot.plotSimpleScatter(x, y, df, save=True, path=output_file)

print('done')





