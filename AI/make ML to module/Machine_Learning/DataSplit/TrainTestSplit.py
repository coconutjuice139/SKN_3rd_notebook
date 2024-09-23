from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from .DataLoad import DataLoad
from .SeedsInfo import reset_seeds


def split_tr_te_and_ori_te():
    ori_train, ori_test = DataLoad.road_data()

    y = ori_train['survived']
    X = ori_train.drop(['survived'], axis=1)

    reset_seeds()
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, stratify=ori_train['survived'])

    print(f'X_tr.shape = {X_tr.shape}, X_te.shape = {X_te.shape}, y_tr.shape = {y_tr.shape}, y_te.shape = {y_te.shape}')
    return X_tr, X_te, y_tr, y_te, ori_test
