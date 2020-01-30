# -*- encoding: utf-8 -*-
'''
@File    :   football_dataset.py
@Time    :   2020/01/30 16:16:52
@Author  :   Yuan Yu
'''

import os
import re
import numpy as np
import six.moves.cPickle as cPickle
from functools import reduce

import torch
from torch.utils.data import Dataset


class FootballDataset(Dataset):
    """Football Dataset"""
    def __init__(self,
                 root_dir='/projects/research/football/dumps',
                 dump_files=None,
                 Tx=60,
                 train=True,
                 transform=None):
        self.root_dir = root_dir
        self.transform = transform

        self.Tx = Tx

        if dump_files is None:
            dump_files = self.get_all_dump_filenames()
            if train is True:
                dump_files = dump_files[:-20]
            else:
                dump_files = dump_files[-20:]

        Xs, Ys, total_m = list(), list(), 0
        for dump_file in dump_files:
            X, Y, m, n_X, n_Y = self._get_XY(dump_file)
            Xs.append(X)
            Ys.append(Y)
            total_m += m
        self.X = np.concatenate(Xs, axis=0)
        self.Y = np.concatenate(Ys, axis=0)
        self.n_X = X.shape[2]
        self.n_Y = Y.shape[2]

    def __len__(self):
        return self.X.shape[0]

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        X_sample = self.X[idx]
        Y_sample = self.Y[idx]
        sample = {'X': X_sample, 'Y': Y_sample}

        if self.transform is not None:
            sample = self.transform(sample)
        return sample

    def get_all_dump_filenames(self):
        def help(dumps, s):
            if re.fullmatch(pattern, s):
                dumps.append("%s/%s" % (self.root_dir, s))
            return dumps

        files = os.listdir(self.root_dir)
        pattern = r'episode_done.*\.dump'
        dumps = reduce(help, files, list())
        return dumps

    def _load_data(self, dump_file):
        """load data from dump"""
        dump_path = os.path.join(self.root_dir, dump_file)

        with open(dump_path, 'rb') as file:
            data = cPickle.load(file)

        balls = np.array([d['observation']['ball'] for d in data])
        left_positions = np.array(
            [d['observation']['left_team'] for d in data])
        right_positions = np.array(
            [d['observation']['right_team'] for d in data])

        data = {
            'balls': balls,
            'left_positions': left_positions,
            'right_positions': right_positions
        }

        return data

    def _get_XY(self, dump_file):
        """get X, Y from dump_file"""
        data = self._load_data(dump_file)
        m = int(data['balls'].shape[0] / self.Tx)
        try:
            X = np.concatenate(
                (data['left_positions'], data['right_positions']),
                axis=1).reshape((m, self.Tx, -1))
        except Exception:
            print(dump_file)
            print(data['left_positions'].shape)

        try:
            Y = data['balls'].reshape((m, self.Tx, -1))
        except Exception:
            print(dump_file)
        n_X = X.shape[2]
        n_Y = Y.shape[2]
        return X, Y, m, n_X, n_Y
