# coding=utf-8

"""help functions to help build a RNN using data from football"""

import six.moves.cPickle as cPickle
import numpy as np


def load_data(dump_path='/projects/research/football/dumps/episode_done_20200105-155830227447.dump'):
	"""load data from dump"""

	with open(dump_path, 'rb') as file:
		data = cPickle.load(file)
	
	balls = np.array( [ d['observation']['ball'] for d in data ] )
	left_positions = np.array( [ d['observation']['left_team'] for d in data ] )
	right_positions = np.array( [ d['observation']['right_team'] for d in data ] )
	
	data = {
		'balls': balls, 
		'left_positions': left_positions, 
		'right_positions': right_positions
	}

	return data

def get_XY(dump_path='/projects/research/football/dumps/episode_done_20200105-155830227447.dump', Tx=60):
	"""get X, Y from dump"""

	data = load_data(dump_path)
	m = int(data['balls'].shape[0]/Tx)
	X = np.concatenate( (data['left_positions'], data['right_positions']), axis=0 ).reshape((m, Tx, -1))
	Y = data['balls'].reshape((m, Tx, -1))
	n_X = X.shape[2]
	n_Y = Y.shape[2]
	return X, Y, m, n_X, n_Y, Tx

def get_train_XY():
	return get_XY(dump_path='/projects/research/football/dumps/episode_done_20200105-155830227447.dump')

def get_test_XY():
	return get_XY(dump_path='/projects/research/football/dumps/episode_done_20200105-190120854468.dump')
