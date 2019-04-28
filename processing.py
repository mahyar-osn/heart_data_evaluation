import os

import pandas as pd
import numpy as np

import hickle as hkl
import json

import read_write_data as io


root = '/hpc/nebr002/Fitting/Fit/FieldFitting/Data'
input_csv = 'evaluated_raw_field_elements_included.csv'


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'to_json'):
            return obj.to_json(orient='records')
        return json.JSONEncoder.default(self, obj)


def get_bin_average(data, sub):
    new_data = np.zeros((600, 17))

    index = 0
    for elem in range(1, 25):
        for bin in range(1, 26):
            new_data[index, 0] = elem
            new_data[index, 1] = bin

            if data['e{0}'.format(elem)]['bin{0}'.format(bin)].shape[0] != 0:
                new_data[index, 2:] = np.hstack((data['e{0}'.format(elem)]['bin{0}'.format(bin)].shape[0],
                                                 np.average(data['e{0}'.format(elem)]['bin{0}'.format(bin)][:, 2:],
                                                            axis=0)))
            else:
                pass

            index += 1

    header = ['Element', 'Bin', 'Cell Number', 'Anisotropy', 'Area3d', 'Elongation', 'EqDiameter',
              'FeretShape3d', 'Length3d', 'Orientation2Phi', 'Orientation2Theta', 'OrientationPhi', 'OrientationTheta',
              'Perimeter', 'Shape_VA3d', 'Volume3d', 'Width3d']

    df = pd.DataFrame(new_data, columns=header)
    df[['Element', 'Bin', 'Cell Number']] = df[['Element', 'Bin', 'Cell Number']].astype(np.int)

    output_dir = os.path.join('dataset', sub)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    df.to_csv((os.path.join(output_dir, 'sorted_data.csv')), sep=',')

    return None


def process_data(sub):
    fieldNames = ['Anisotropy', 'Area3d', 'Elongation', 'EqDiameter', 'FeretShape3d', 'Length3d', 'Orientation2Phi',
                  'Orientation2Theta', 'OrientationPhi', 'OrientationTheta', 'Perimeter', 'Shape_VA3d', 'Volume3d',
                  'Width3d']

    subject = sub
    nrows = _get_number_of_rows(subject, fieldNames[0])

    data = np.zeros((nrows, len(fieldNames) + 4))
    datalist = list()

    for field in fieldNames:
        fname = io.setup_path(os.path.join(root, subject), field, input_csv)
        if field == 'Anisotropy':
            d = io.get_raw_field(fname)
        else:
            d = io.get_raw_field(fname, use_cols=[field])
        datalist.append(d)

    data[:, 0:5] = datalist[0]
    for i in range(len(fieldNames) - 1):
        data[:, i + 5] = datalist[i + 1].reshape(datalist[i + 1].shape[0])

    dataset = make_bins(data)

    output_dir = 'dataset/' + subject
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    hkl.dump(dataset, output_dir + '/data.hkl', mode='w', compression='gzip')

    return None


def _get_number_of_rows(sub, field):
    return io.get_raw_field(io.setup_path(os.path.join(root, subject), field, input_csv)).shape[0]


def make_bins(d, bins=5):
    """

    :param d:
    :param bins:
    :return:
    """

    bin_size = bins
    nelements = 24

    data = d

    element_dict = dict()
    for x in range(1, nelements + 1):
        element_dict['e{0}'.format(x)] = dict()
        for y in range(1, bin_size * bin_size + 1):
            d = {'bin{0}'.format(y): list()}
            element_dict['e{0}'.format(x)].update(d)

    for point in data:
        xi1 = point[2]
        xi2 = point[3]

        elem_num = int(point[1])

        for element in range(1, len(element_dict) + 1):
            if elem_num == element:
                counter = 1
                for x in range(bin_size):
                    for y in range(bin_size):
                        if y == 0 and x == 0:
                            if float(y) / bin_size <= xi1 <= (float(y) + 1.) / bin_size and float(
                                    x) / bin_size <= xi2 <= (float(x) + 1.) / bin_size:
                                values = point[2:].tolist()
                                element_dict['e{0}'.format(element)]['bin{0}'.format(counter)].append(values)

                        elif y == 0 and x != 0:
                            if float(y) / bin_size <= xi1 <= (float(y) + 1.) / bin_size and float(
                                    x) / bin_size < xi2 <= (float(x) + 1.) / bin_size:
                                values = point[2:].tolist()
                                element_dict['e{0}'.format(element)]['bin{0}'.format(counter)].append(values)

                        elif y != 0 and x == 0:
                            if float(y) / bin_size < xi1 <= (float(y) + 1.) / bin_size and float(
                                    x) / bin_size <= xi2 <= (float(x) + 1.) / bin_size:
                                values = point[2:].tolist()
                                element_dict['e{0}'.format(element)]['bin{0}'.format(counter)].append(values)

                        elif y != 0 and x != 0:
                            if float(y) / bin_size < xi1 <= (float(y) + 1.) / bin_size and float(
                                    x) / bin_size < xi2 <= (float(x) + 1.) / bin_size:
                                values = point[2:].tolist()
                                element_dict['e{0}'.format(element)]['bin{0}'.format(counter)].append(values)

                        counter += 1

    for elem in element_dict.keys():
        for k, v in element_dict[elem].items():
            element_dict[elem][k] = np.asarray(v)

    return element_dict


if __name__ == '__main__':
    subject = '59'
    data_root_path = '/hpc/mosa004/Nazanin_Heart_fitting/Heart_2/FieldFitting/evaluate/dataset'
    data_file = os.path.join(data_root_path, subject, 'data.hkl')

    data = hkl.load(data_file)
    get_bin_average(data, subject)

    print("done")
