# -*- encoding: utf-8 -*-
'''
@File    :   basic_nn.py
@Time    :   2020/01/30 16:16:31
@Author  :   Yuan Yu
'''

import torch.nn as nn


# Fully connected neural network with one hidden layer
class BasicNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(BasicNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out
