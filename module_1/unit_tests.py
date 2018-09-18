import os
import sys
import tempfile

import pandas as pd


def dataset_types(data):
    if data.__class__.__name__ == 'ndarray':
        print('dataset has type: \n', data.__class__.__name__)
    else:
        print('dataset type is \n:',data.__class__.__name__)
        print('and changed to \n: ',data.__class__.__name__)


from traceback import print_exc

class CustomException(Exception): pass

def check_ty(data):
    try:
        raise CustomException("hi")
    except Exception:
        print('type is:', data.__class__.__name__)
    print_exc()


def micro_data(index=None):

    cols = ['type', 'x1', 'x2', 'x3','x4', 'x5', 'x6', 'x7', 'x8','x9','x10']
    df = pd.DataFrame(columns=cols)
    d0 = ['train'] + [0.68272, 0.34332, 0.37377, 0.60618, 0.52544, 0.57740, 0.43416,12,0.5, 0]
    d1 = ['train'] + [0.47382, 0.54013, 0.40763, 0.57723, 0.69972, 0.31182, 0.45172,11,0.4, 0]
    d2 = ['train'] + [0.54065, 0.38867, 0.33660, 0.33699, 0.33615, 0.64675, 0.57937,17,0.4, 1]
    d3 = ['train'] + [0.36597, 0.34767, 0.23873,0.49338, 0.57128, 0.60922, 0.61345,19,0.3, 0]
    d4 = ['train'] + [0.43416, 0.45172, 0.57937, 0.49922, 0.48688, 0.49413,0.39642,10,0.6,0]
    d5 = ['train'] + [0.39889, 0.32397, 0.47546, 0.64955, 0.65867, 0.49308, 0.54065,9,0.6, 0]
    d6 = ['train'] + [0.39122, 0.6460351, 0.59575, 0.64499, 0.40582, 0.54648, 0.40582,15,0.7, 1]
    d7 = ['train'] + [0.50341, 0.40711, 0.58961, 0.47149, 0.44292, 0.69205, 0.69205,20,0.6, 1]
    d8 = ['train'] + [0.41928, 0.78092, 0.54567, 0.67296, 0.38246, 0.54248, 0.49338,1,0.5, 0]
    d9 = ['train'] + [0.44145, 0.54494, 0.48378, 0.45234, 0.42701, 0.55697, 0.55697,4,0.4, 1]
    d10 = ['train'] + [0.42138, 0.55323, 0.48599, 0.52296, 0.48610, 0.50239, 0.48599,12,0.4, 1]
    d11 = ['train'] + [0.39122, 0.54343, 0.43096, 0.52507, 0.69093, 0.53813, 0.69093,7,0.5, 0]
    d12 = ['train'] + [0.50341, 0.45878, 0.45197, 0.33503, 0.54502, 0.57808, 0.54502,20,0.7, 1]
    d13 = ['train'] + [0.41928, 0.49877, 0.49933, 0.57899, 0.58098, 0.39557, 0.58098, 30,0.4, 0]
    d14 = ['train'] + [0.44145, 0.32009, 0.30889, 0.56424, 0.52576, 0.54895, 0.42701,30,0.2, 1]
    d15 = ['train'] + [0.42138, 0.52133, 0.29764, 0.52538, 0.57167, 0.49572, 0.18624,50,0.4, 1]
    d16 = ['train'] + [0.42138, 0.52505, 0.64891, 0.45036, 0.18624, 0.44906, 0.56424,12,0.4, 1]
    d17 = ['train'] + [0.39122, 0.60458, 0.63060, 0.50317, 0.29515, 0.42842, 0.56424,12,0.6, 0]
    d18 = ['test'] + [0.50341, 0.49887, 0.82889, 0.33503, 0.37323, 0.25430, 0.56424,20,0.4, 1]
    d19 = ['test'] + [0.41928, 0.27080, 0.46121, 0.57899, 0.47978, 0.49140, 0.47978,4,0.5, 0]
    d20 = ['test'] + [0.44145, 0.49877, 0.58961, 0.56424, 0.52576, 0.39557, 0.52576,1,0.2, 1]
    d21 = ['test'] + [0.42138, 0.32009, 0.63060, 0.56424, 0.29515, 0.53813, 0.29515,50,0.2, 1]

    df.loc['index0'] = d0
    df.loc['index1'] = d1
    df.loc['index2'] = d2
    df.loc['index3'] = d3
    df.loc['index4'] = d4
    df.loc['index5'] = d5
    df.loc['index6'] = d6
    df.loc['index7'] = d7
    df.loc['index8'] = d8
    df.loc['index9'] = d9
    df.loc['index10'] = d10
    df.loc['index11'] = d11
    df.loc['index12'] = d12
    df.loc['index13'] = d13
    df.loc['index14'] = d14
    df.loc['index15'] = d15
    df.loc['index16'] = d16
    df.loc['index17'] = d17
    df.loc['index18'] = d18
    df.loc['index19'] = d19
    df.loc['index20'] = d20
    df.loc['index21'] = d21

    if index is not None:
        df = df.iloc[index]
    df = df.copy()  # assure contiguous memory
    data = df
    return data
