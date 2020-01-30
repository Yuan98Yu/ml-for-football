# -*- encoding: utf-8 -*-
'''
@File    :   test_logger.py
@Time    :   2020/01/30 16:16:11
@Author  :   Yuan Yu
'''

from six.moves.cPickle import dump
from os.path import join


class TestLogger:
    def __init__(self, logfile_root):
        self.logfile_root = logfile_root

    def dump(self, anomalies, test_dataset, threshold, output_file):
        log = {
            'anomalies_number': len(anomalies),
            'test_number': test_dataset[:]['X'].shape[0]*test_dataset[:]['X'].shape[1],
            'threshold': threshold,
            'anomalies': anomalies
        }

        with open(join(self.logfile_root, output_file), 'wb') as f:
            dump(log, f)
