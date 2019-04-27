import os

import pandas as pd
import numpy as np


def setup_path(path, field, fname):
    csv_field_file = os.path.join(path, field, 'FieldFit', fname)

    return csv_field_file


def get_raw_field(filename, use_cols=None):
    """

    :param filename:
    :param use_cols:
    :return:
    """

    return np.asarray(_read_csv(filename, sep=',', header=0, skiprow=None, use_cols=use_cols), dtype=np.float64)


def _read_csv(filename, sep=',', header=None, skiprow=None, use_cols=None):
    """
    Method to read csv using panda lib.

    :param filename: This is the path to the csv file
    :param sep: This is the delimiter used to separate data in the csv file
    :param header: Specify the header row number.
    :return: Data frame.
    """

    fn = filename
    fr = pd.read_csv(fn, sep=sep, header=header, skiprows=skiprow, usecols=use_cols)

    return fr
