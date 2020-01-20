# coding=utf-8

"""help functions to get data from football's dumps"""

import six.moves.cPickle as cPickle
import numpy as np
import re
import os
from functools import reduce


def load_data(dump_path='/projects/research/football/dumps/episode_done_20200105-155830227447.dump'):
	"""load data from dump"""

	with open(dump_path, 'rb') as file:
		data = cPickle.load(file)

	balls = np.array([d['observation']['ball'] for d in data])
	left_positions = np.array([d['observation']['left_team'] for d in data])
	right_positions = np.array([d['observation']['right_team'] for d in data])

	data = {
		'balls': balls,
		'left_positions': left_positions,
		'right_positions': right_positions
	}

	return data


def get_all_dump_filenames(dir='/projects/research/football/dumps'):
	def help(dumps, s):
		if re.fullmatch(pattern, s):
			dumps.append("%s/%s" % (dir, s))
		return dumps

	files = os.listdir(dir)
	pattern = r'episode_done.*\.dump'
	dumps = reduce(help, files, list())
	return dumps


def get_XY(dump_path='/projects/research/football/dumps/episode_done_20200105-155830227447.dump', Tx=60):
	"""get X, Y from dump"""

	data = load_data(dump_path)
	m = int(data['balls'].shape[0]/Tx)
	try:
		X = np.concatenate(
			(data['left_positions'], data['right_positions']), axis=1).reshape((m, Tx, -1))
	except:
		print(dump_path)
		print(data['left_positions'].shape)

	try:
		Y = data['balls'].reshape((m, Tx, -1))
	except:
		print(dump_path)
	n_X = X.shape[2]
	n_Y = Y.shape[2]
	return X, Y, m, n_X, n_Y, Tx


def load_all_dumps():
	dump_paths = get_all_dump_filenames()

	Xs, Ys, total_m = list(), list(), 0
	for dump in dump_paths:
		X, Y, m, n_X, n_Y, Tx = get_XY(dump, Tx=60)
		Xs.append(X)
		Ys.append(Y)
		total_m += m
	X = np.concatenate(Xs, axis=0)
	Y = np.concatenate(Ys, axis=0)
	n_X = X.shape[2]
	n_Y = Y.shape[2]
	Tx = X.shape[1]
	
	return X, Y, total_m, n_X, n_Y, Tx


def split_train_test(X, Y, test_size):
	X_train, Y_train = X[:-test_size], Y[:-test_size] 
	X_test, Y_test = X[-test_size:], Y[-test_size:]

	return X_train, Y_train, X_test, Y_test


def get_train_XY():
	return get_XY(dump_path='/projects/research/football/dumps/episode_done_20200105-155830227447.dump')


def get_test_XY():
	return get_XY(dump_path='/projects/research/football/dumps/episode_done_20200105-190120854468.dump')


def check(dump_path='/projects/research/football/dumps/episode_done_20200105-155830227447.dump', Tx=60):
	"""get X, Y from dump"""

	data = load_data(dump_path)
	print(dump_path)
	print(data['left_positions'].shape)


def check_all():
	dumps = get_all_dump_filenames()
	for dump in dumps:
		check(dump)
