import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from . import FilePath

class DataLoad:
    def __init__(self):
        plt.style.use('fivethirtyeight')
        plt.ion()
        import warnings
        warnings.filterwarnings('ignore')

    def road_data(self):
        args = FilePath.make_easydict()
        ori_train = pd.read_csv(args.train_csv)
        ori_test = pd.read_csv(args.test_csv)
        return ori_train, ori_test