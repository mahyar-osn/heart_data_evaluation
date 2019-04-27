import os

import pandas as pd
import numpy as np


root = '/hpc/nebr002/Fitting/Fit/FieldFitting/Data'


def setup_path(subject, field):

    ipdata_path = os.path.join(root, subject, field, field+'.ipdata')
    ipxi_path = os.path.join(root, subject, field, 'FieldFit', 'fitted_field_xi.ipxi')

    return ipdata_path, ipxi_path


def read_csv(filename, sep=',', header=None, skiprow=None):
    """
    Method to read csv using panda lib.

    :param filename: This is the path to the csv file
    :param sep: This is the delimiter used to separate data in the csv file
    :param header: Specify the header row number.
    :return: Data frame.
    """

    fn = filename
    fr = pd.read_csv(fn, sep=sep, header=header, skiprows=skiprow)

    return fr


def get_ipxi(filename):
    """
    Read .ipxi file format and store values in array.

    :param filename: File name.
    :return: Numpy array.
    """
    ipxi_df = read_csv(filename, sep='\s+')

    return np.asarray(ipxi_df.ix[:, 0:3], dtype=np.float64)


def get_ipdata(filename):
    """
     Read .ipdata file format and store values in array.

    :param filename: File name
    :return: Numpy array
    """

    ipdata_df = read_csv(filename, sep='\s+', skiprow=None)

    return np.asarray(ipdata_df.ix[:, 4], dtype=np.float64).reshape(ipdata_df.shape[0], 1)


def write_xidata():

    fields = ['Length3d',
              'Width3d',
              'FeretShape3d',
              'Area3d',
              'EqDiameter',
              'Orientation2Phi',
              'Orientation2Theta',
              'OrientationPhi',
              'OrientationTheta',
              'Perimeter',
              'Shape_VA3d',
              'Volume3d',
              'Elongation',
              'Anisotropy']

    # subjects = ['50', '52', '53', '59']
    subjects = ['53', '59']

    for subject in subjects:
        for field in fields:
            ipdata_filename, ipxi_filename = setup_path(subject, field)

            ipdata = get_ipdata(ipdata_filename)
            ipxi = get_ipxi(ipxi_filename)
            merged = np.hstack([ipxi, ipdata])
            header = ['index', 'element', 'xi1', 'xi2', field]
            final = np.vstack([header, merged])
            output_csv = os.path.join(root, subject, field, 'FieldFit', 'evaluated_raw_field_elements_included.csv')
            np.savetxt(output_csv, final, ['%s', '%s', '%s', '%s', '%s'], delimiter=',')
            # print(json.dumps(final, default=lambda x: list(x), indent=4))

            print("Field * ", field, " * for subject * ", subject, " * completed.")

    return None


if __name__ == '__main__':
    write_xidata()
